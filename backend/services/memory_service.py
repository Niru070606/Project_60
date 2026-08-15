from repositories.conversation_repository import get_or_create_conversation
from repositories.memory_repository import (
    save_memory,
    get_memories,
    find_similar_memory,
    update_memory,
    delete_memory,
    delete_all_memories
    
)

from services.memory.embedding_service import (
    create_and_store_embedding,
)

from repositories.transaction_repository import (
    flush,
    commit,
    rollback,
)

def create_memory(
    memory: str,
    category: str,
    importance: int,
    ):
    
    conversation = get_or_create_conversation()

    try:

        memory_record = save_memory(
            conversation_id=conversation.id,
            memory=memory,
            category=category,
            importance=importance,
        )
        
        flush()

        create_and_store_embedding(
            memory_record.id,
            memory,
        )

        commit()

        return memory_record

    except Exception:

        rollback()

        raise




def load_memories(limit: int = 10):

    conversation = get_or_create_conversation()

    return get_memories(
        conversation.id,
        limit=limit,
    )

def save_extracted_memories(memories):

    print("\n===== REFLECTION MEMORIES RECEIVED =====")
    print(memories)
    print("========================================")


    conversation = get_or_create_conversation()

    saved_memories = []

    for memory in memories:

        confidence = memory.get(
            "confidence",
            100
        )

        if confidence < 80:
            continue

        existing = find_similar_memory(
            conversation.id,
            memory["memory"],
        )

        print("===== SIMILAR MEMORY CHECK =====")
        print("New:", memory["memory"])
        print("Existing:", existing)
        print("================================")

        if existing:

            update_memory(
                existing,
                memory["memory"],
                memory["importance"],
            )

            saved_memories.append(
                existing
            )

        else:

            print("🔥 CREATING NEW MEMORY:", memory["memory"])

            memory_record = create_memory(
                memory=memory["memory"],
                category=memory["category"],
                importance=memory["importance"],
            )

            saved_memories.append(
                memory_record
            )

    return saved_memories

def remove_memory(memory):
    delete_memory(memory)

def reinforce_memories(memories, amount=1):

    for memory in memories:

        new_importance = min(
            memory.importance + amount,
            100
        )

        update_memory(
            memory,
            memory.memory,
            new_importance,
            )

def replace_memories(memories):

    conversation = get_or_create_conversation()

    delete_all_memories(conversation.id)

    for memory in memories:

        save_memory(
            conversation_id=conversation.id,
            memory=memory["memory"],
            category=memory["category"],
            importance=memory["importance"],
        )

def create_missing_embedding(memory):
    from repositories.memory_embedding_repository import (
        get_embedding_by_memory_id,
    )

    existing = get_embedding_by_memory_id(memory.id)

    if existing:
        return existing

    return create_and_store_embedding(
        memory.id,
        memory.memory,
    )