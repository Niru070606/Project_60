from dataclasses import dataclass


@dataclass
class BrainContext:

    # ========= Core =========

    intent: str = ""

    thought: object | None = None
    thought_prompt: str = ""

    behavior: object | None = None
    behavior_prompt: str = ""

    # ========= Prompt Sections =========

    identity: str = ""

    personality: str = ""

    relationship: str = ""

    memory: str = ""

    history: str = ""

    rules: str = ""

    # ========= Future Modules =========

    mood: str = ""

    goals: str = ""

    # ========= Final =========

    system_prompt: str = ""