from services.memory_search_service import search_memories
from services.prompts.memory_prompt import build_memory_prompt


def build_memory(user_message: str, limit: int = 5,):

    memories = search_memories(
        user_message,
        limit=limit,
    )
    print("\n=== Memories Sent To Prompt ===")
    for memory in memories:
        print(memory.memory)
    print("===============================\n")

    return build_memory_prompt(
        memories
    )