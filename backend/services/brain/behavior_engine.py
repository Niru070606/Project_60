from dataclasses import dataclass


@dataclass
class Behavior:

    tone: str = "normal"

    response_length: str = "medium"

    explain_step_by_step: bool = False

    ask_follow_up: bool = False

    validate_emotion: bool = False

def create_behavior(thought):

    behavior = Behavior()

    if thought.answer_style == "warm":
        behavior.tone = "warm"
        behavior.validate_emotion = True

    elif thought.answer_style == "technical":
        behavior.tone = "professional"
        behavior.explain_step_by_step = True

    elif thought.answer_style == "detailed":
        behavior.response_length = "long"
        behavior.explain_step_by_step = True
        behavior.ask_follow_up = True

    elif thought.answer_style == "precise":
        behavior.response_length = "short"

    return behavior