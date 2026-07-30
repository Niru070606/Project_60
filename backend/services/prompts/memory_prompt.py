def build_memory_prompt(memories):

    if not memories:
        return ""

    prompt = """
=========================
LONG-TERM MEMORY
=========================

These are verified long-term memories about the user.

Treat every memory below as factual unless the user explicitly corrects it.

When the user asks:
- what you know about them,
- what you remember,
- who they are,
- or asks about their preferences,

ALWAYS answer using these memories.

Do NOT say "I don't remember" if the answer exists below.

Use these memories naturally in conversation.

Verified memories:

"""

    for memory in memories:
        prompt += f"- {memory.memory}\n"

    return prompt