from services.relationship_service import get_relationship
from services.prompts.relationship_prompt import build_relationship_prompt


def build_relationship():

    relationship = get_relationship()

    return build_relationship_prompt(
        relationship
    )