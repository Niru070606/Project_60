from dataclasses import dataclass, field

@dataclass
class BrainContext:

    # Core Identity
    identity: str = ""

    # Personality Prompt
    personality: str = ""

    # Relationship Prompt
    relationship: str = ""

    # Memory Prompt
    memory: str = ""

    # Rules
    rules: str = ""

    # Conversation History
    history: str = ""

    # Future
    mood: str = ""
    goals: str = ""
    intent: str = ""

    # Final Prompt
    system_prompt: str = ""