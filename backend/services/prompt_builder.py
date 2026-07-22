from services.prompts.role_prompt import build_role_prompt
from services.prompts.personality_prompt import build_personality_prompt
from services.prompts.memory_prompt import build_memory_prompt


def build_system_prompt(
    personality: dict,
    memories: list = None,
) -> str:

    return "\n\n".join([
        build_personality_prompt(personality),
        build_role_prompt(),
        build_memory_prompt(memories),
    ])