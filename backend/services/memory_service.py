from repositories.conversation_repository import get_or_create_conversation
from repositories.memory_repository import (
    save_memory,
    get_memories,
    find_similar_memory,
    update_memory,
    delete_memory,
    delete_all_memories
    
)

def create_memory(
    memory: str,
    category: str,
    importance: int,
):
    conversation = get_or_create_conversation()

    return save_memory(
        conversation_id=conversation.id,
        memory=memory,
        category=category,
        importance=importance,
    )


def load_memories(limit: int = 10):

    conversation = get_or_create_conversation()

    return get_memories(
        conversation.id,
        limit=limit,
    )

def save_extracted_memories(memories):

    conversation = get_or_create_conversation()

    for memory in memories:

        confidence = memory.get("confidence", 100)

        if confidence < 80:
            continue

        existing = find_similar_memory(
            conversation.id,
            memory["memory"],
        )

        if existing:

            update_memory(
                existing,
                memory["memory"],
                memory["importance"],
            )

        else:

            save_memory(
                conversation_id=conversation.id,
                memory=memory["memory"],
                category=memory["category"],
                importance=memory["importance"],
            )

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
