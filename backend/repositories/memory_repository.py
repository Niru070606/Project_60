from difflib import SequenceMatcher

from database import db
from models.memory import Memory


def save_memory(
    conversation_id: int,
    memory: str,
    category: str,
    importance: int,
):
    mem = Memory(
        conversation_id=conversation_id,
        memory=memory,
        category=category,
        importance=importance,
    )

    db.session.add(mem)
    db.session.commit()

    return mem


def get_memories(
    conversation_id: int,
    limit: int | None = None,
):

    query = (
        Memory.query
        .filter_by(conversation_id=conversation_id)
        .order_by(Memory.importance.desc())
    )

    if limit:
        query = query.limit(limit)

    return query.all()


def delete_memory(memory: Memory):
    db.session.delete(memory)
    db.session.commit()

def find_memory(
    conversation_id: int,
    memory: str,
):
    return (
        Memory.query
        .filter_by(
            conversation_id=conversation_id,
            memory=memory,
        )
        .first()
    )

def update_memory(
    memory: Memory,
    new_text: str,
    importance: int,
):

    # Only replace the memory if the new version
    # contains more information.
    if len(new_text) > len(memory.memory):
        memory.memory = new_text

    memory.importance = max(
        memory.importance,
        importance,
    )

    db.session.commit()

def increment_retrieval_count(
    memory: Memory,
):
    memory.retrieval_count += 1

    db.session.commit()

def find_similar_memory(
    conversation_id: int,
    new_memory: str,
    threshold: float = 0.85,
):

    memories = (
        Memory.query
        .filter_by(conversation_id=conversation_id)
        .all()
    )

    best_match = None
    best_score = 0

    for memory in memories:

        score = SequenceMatcher(
            None,
            memory.memory.lower(),
            new_memory.lower(),
        ).ratio()

        if score > best_score:
            best_score = score
            best_match = memory

    if best_score >= threshold:
        return best_match

    return None