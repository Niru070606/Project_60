from services.brain.context import BrainContext

from services.brain.identity import build_identity
from services.brain.relationship import build_relationship
from services.brain.memory import build_memory
from services.brain.history import build_history
from services.brain.rules import build_rules
from services.brain.intent import detect_intent

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

    memory_limit = get_memory_limit(brain.intent)
    history_limit = get_history_limit(brain.intent)

    print("Memory Limit:", memory_limit)
    print("History Limit:", history_limit)

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

    sections = []

    if brain.identity:
        sections.append(brain.identity)

    if brain.relationship:
        sections.append(brain.relationship)

    if brain.memory:
        sections.append(brain.memory)

    if brain.rules:
        sections.append(brain.rules)

    brain.system_prompt = "\n\n".join(sections)

    # print("========== BRAIN ==========")
    # print("Intent:", brain.intent)
    # print("Identity:", bool(brain.identity))
    # print("Relationship:", bool(brain.relationship))
    # print("Memory:", bool(brain.memory))
    # print("Rules:", bool(brain.rules))
    # print("History:", bool(brain.history))
    # print("===========================")

    return brain