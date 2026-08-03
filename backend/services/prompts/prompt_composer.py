from services.prompts.prompt_layouts import (
    DEFAULT_LAYOUT,
    PROGRAMMING_LAYOUT,
    RELATIONSHIP_LAYOUT,
    MEMORY_LAYOUT,
)

def get_layout(intent):

    if intent == "programming":
        return PROGRAMMING_LAYOUT

    if intent == "relationship":
        return RELATIONSHIP_LAYOUT

    if intent == "memory":
        return MEMORY_LAYOUT

    return DEFAULT_LAYOUT

def compose_prompt(brain):

    layout = get_layout(brain.intent)

    mapping = {
        "identity": brain.identity,
        "relationship": brain.relationship,
        "behavior": brain.behavior_prompt,
        "memory": brain.memory,
        "thought": brain.thought_prompt,
        "rules": brain.rules,
    }

    sections = []

    for section_name in layout:

        section = mapping.get(section_name)

        if section:
            sections.append(section)

    return "\n\n".join(sections)