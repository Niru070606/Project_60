from services.memory_search_service import search_memories
from services.prompts.memory_prompt import build_memory_prompt


def build_memory(user_message: str):

    memories = search_memories(user_message)

    return build_memory_prompt(
        memories
    )