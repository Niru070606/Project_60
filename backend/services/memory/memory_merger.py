import json

from repositories.memory_repository import get_memories
from database import db
from models.memory import Memory
from models.memory_entity import MemoryEntity
from models.entity import Entity


def _get_llm_client():
    """Lazy import to avoid circular dependency. Uses v1beta for system_instruction support."""
    from google import genai
    from google.genai import types
    from config import Config

    client = genai.Client(
        api_key=Config.GEMINI_API_KEY,
        http_options={'api_version': 'v1beta'}
    )
    return client, types


MERGE_PROMPT = """
You are Project-60's memory consolidation engine.

You are given a group of related memories that describe overlapping or similar information.

Your task is to merge them into ONE concise, comprehensive memory that preserves all important information.

Rules:
1. Combine overlapping facts into a single statement
2. Keep the most specific/detailed version of each fact
3. Preserve entity names, dates, preferences, goals
4. Remove redundancy
5. Output only the merged memory text, category, and importance (0-100)

Input format: List of memories with their categories and importance scores.

Output format (JSON only):
{
  "memory": "Merged memory text...",
  "category": "Category",
  "importance": 85
}
"""


def find_merge_candidates(memories, threshold=0.75):
    """
    Find groups of memories that should be merged.
    Uses text similarity to find candidates.
    """
    from difflib import SequenceMatcher

    candidates = []
    used = set()

    for i, mem1 in enumerate(memories):
        if mem1.id in used:
            continue

        group = [mem1]
        used.add(mem1.id)

        for j, mem2 in enumerate(memories):
            if i == j or mem2.id in used:
                continue

            score = SequenceMatcher(
                None,
                mem1.memory.lower(),
                mem2.memory.lower()
            ).ratio()

            if score >= threshold:
                group.append(mem2)
                used.add(mem2.id)

        if len(group) > 1:
            candidates.append(group)

    return candidates


def merge_memory_group(memory_group):
    """
    Use LLM to merge a group of similar memories into one.
    """
    if len(memory_group) <= 1:
        return None

    client, types = _get_llm_client()

    memories_text = "\n".join([
        f"- [{m.category}] (imp: {m.importance}) {m.memory}"
        for m in memory_group
    ])

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Merge these memories:\n{memories_text}",
        config=types.GenerateContentConfig(
            system_instruction=MERGE_PROMPT,
            response_mime_type="application/json",
        ),
    )

    try:
        result = json.loads(response.text)
        return result
    except json.JSONDecodeError:
        return None


def merge_and_update(memory_group, merged_result):
    """
    Replace the memory group with the merged memory.
    Preserves entity links by transferring them to the new memory.
    """
    if not merged_result:
        return None

    # Create new merged memory
    new_memory = Memory(
        conversation_id=memory_group[0].conversation_id,
        memory=merged_result["memory"],
        category=merged_result["category"],
        importance=merged_result["importance"],
    )
    db.session.add(new_memory)
    db.session.flush()

    # Collect all entity links from the group
    entity_ids = set()
    memory_ids = [mem.id for mem in memory_group]

    for mem in memory_group:
        links = MemoryEntity.query.filter_by(memory_id=mem.id).all()
        for link in links:
            entity_ids.add(link.entity_id)

    # Delete memory embeddings for old memories first (FK constraint)
    from models.memory_embedding import MemoryEmbedding
    MemoryEmbedding.query.filter(MemoryEmbedding.memory_id.in_(memory_ids)).delete(synchronize_session=False)

    # Delete old memory-entity links (FK constraint)
    MemoryEntity.query.filter(MemoryEntity.memory_id.in_(memory_ids)).delete(synchronize_session=False)

    # Link new memory to all collected entities
    for entity_id in entity_ids:
        link = MemoryEntity(memory_id=new_memory.id, entity_id=entity_id)
        db.session.add(link)

    # Delete old memories
    for mem in memory_group:
        db.session.delete(mem)

    db.session.commit()

    # Create embedding for new merged memory
    from services.memory.embedding_service import create_and_store_embedding
    create_and_store_embedding(new_memory.id, new_memory.memory)

    return new_memory


def run_memory_merge(conversation_id, similarity_threshold=0.75):
    """
    Main function to run memory consolidation for a conversation.
    Returns number of merges performed.
    """
    memories = get_memories(conversation_id, limit=None)

    if len(memories) < 2:
        return 0

    merge_groups = find_merge_candidates(memories, similarity_threshold)

    merges_done = 0
    for group in merge_groups:
        merged = merge_memory_group(group)
        if merged:
            new_mem = merge_and_update(group, merged)
            if new_mem:
                merges_done += 1
                print(f"Merged {len(group)} memories into 1: {merged['memory'][:60]}...")

    return merges_done


def auto_merge_on_new_memory(conversation_id, new_memory_text, new_memory_id):
    """
    Check if a newly created memory should be merged with existing ones.
    Runs immediately after memory creation.
    """
    memories = get_memories(conversation_id, limit=50)

    from difflib import SequenceMatcher

    best_match = None
    best_score = 0.0

    for mem in memories:
        if mem.id == new_memory_id:
            continue

        score = SequenceMatcher(
            None,
            mem.memory.lower(),
            new_memory_text.lower()
        ).ratio()

        if score > best_score and score >= 0.80:
            best_score = score
            best_match = mem

    if best_match:
        # Merge the two
        merged = merge_memory_group([best_match, Memory(
            id=new_memory_id,
            conversation_id=conversation_id,
            memory=new_memory_text,
            category="",  # Will be filled from best_match if needed
            importance=0
        )])

        if merged:
            merge_and_update([best_match, Memory(
                id=new_memory_id,
                conversation_id=conversation_id,
                memory=new_memory_text,
                category=best_match.category,
                importance=best_match.importance
            )], merged)
            return True

    return False