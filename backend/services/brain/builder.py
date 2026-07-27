from services.brain.identity import build_identity
from services.brain.relationship import build_relationship
from services.brain.memory import build_memory
from services.brain.history import build_history
from services.brain.rules import build_rules


def build_brain(user_message: str):

    return {
        "system_prompt": "\n\n".join([
            build_identity(),
            build_relationship(),
            build_memory(user_message),
            build_rules(),
        ]),
        "history": build_history(),
    }