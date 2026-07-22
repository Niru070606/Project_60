def build_memory_prompt(memories):

    if not memories:
        return ""

    prompt = """
=========================
WHAT YOU KNOW ABOUT THE USER
=========================

The following are long-term memories about the user.

These memories are facts you remember.

They DO NOT change your personality.

Use them naturally during conversation.

Do not list them unless the user asks what you remember.

"""

    for memory in memories:
        prompt += f"- {memory.memory}\n"

    return prompt