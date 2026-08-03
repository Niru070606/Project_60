from dataclasses import dataclass
from services.brain.intent import detect_intent

@dataclass
class ThoughtPlan:

    answer_style: str = "normal"

    ask_follow_up: bool = False

    recall_memory: bool = False

    emotional: bool = False

    teaching: bool = False


def create_thought_plan(user_message: str):

    plan = ThoughtPlan()

    intent = detect_intent(user_message)

    if intent == "memory":
        plan.recall_memory = True
        plan.answer_style = "precise"

    elif intent == "relationship":
        plan.emotional = True
        plan.answer_style = "warm"

    elif intent == "learning":
        plan.teaching = True
        plan.ask_follow_up = True
        plan.answer_style = "detailed"

    elif intent == "programming":
        plan.teaching = True
        plan.answer_style = "technical"

    else:
        plan.answer_style = "normal"

    return plan