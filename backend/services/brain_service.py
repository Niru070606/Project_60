from services.personality_service import get_personality
from services.memory_search_service import search_memories
from services.history_service import get_recent_messages
from services.prompt_builder import build_system_prompt


def build_brain(user_message: str):

    personality = get_personality()

    memories = search_memories(user_message)

    history = get_recent_messages()

    prompt = build_system_prompt(
        personality=personality,
        memories=memories,
        history=history,
    )

    return prompt