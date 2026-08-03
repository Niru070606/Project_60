from services.brain.context import BrainContext
from services.debug.brain_debugger import debug_brain

from services.brain.identity import build_identity
from services.brain.relationship import build_relationship
from services.brain.memory import build_memory
from services.brain.history import build_history
from services.brain.rules import build_rules
from services.brain.intent import detect_intent
from services.brain.thought_engine import create_thought_plan

from services.brain.behavior_engine import create_behavior
from services.prompts.thought_prompt import build_thought_prompt

from services.prompts.prompt_composer import compose_prompt
from services.prompts.behavior_prompt import build_behavior_prompt

from services.brain.context_manager import (
    should_load_identity,
    should_load_memory,
    should_load_relationship,
    should_load_history,
    should_load_rules,
)

from services.brain.context_budget import (
    get_memory_limit,
    get_history_limit,
)



def build_brain(user_message):

    brain = BrainContext()

    brain.intent = detect_intent(user_message)

    brain.thought = create_thought_plan(user_message)
    brain.thought_prompt = build_thought_prompt(
        brain.thought
    )

    brain.behavior = create_behavior(
        brain.thought
    )
    brain.behavior_prompt = build_behavior_prompt(
        brain.behavior
    )

    memory_limit = get_memory_limit(brain.intent)
    history_limit = get_history_limit(brain.intent)

    

    if should_load_identity(brain.intent):
        brain.identity = build_identity()

    if should_load_relationship(brain.intent):
        brain.relationship = build_relationship()

    if should_load_memory(brain.intent):
        brain.memory = build_memory(
            user_message,
            limit=memory_limit,
        )

    if should_load_rules(brain.intent):
        brain.rules = build_rules()

    if should_load_history(brain.intent):
        brain.history = build_history(
            limit=history_limit,
            )

    brain.system_prompt = compose_prompt(brain)


    debug_brain(brain)

    

    return brain