from services.personality_service import get_personality
from services.prompts.personality_prompt import build_personality_prompt


def build_identity():

    personality = get_personality()

    return build_personality_prompt(
        personality
    )