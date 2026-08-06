from services.memory.search_engine import search
from services.prompts.memory_prompt import build_memory_prompt


def build_memory(user_message: str, limit: int = 5,):

    memories = search(
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