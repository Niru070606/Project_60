import json

from google.genai import types

from services.chat_service import client

from services.prompts.memory_consolidation_prompt import (
    build_memory_consolidation_prompt,
)

def consolidate_memories(memories):

    prompt = build_memory_consolidation_prompt()

    memory_text = ""

    for memory in memories:
        memory_text += (
            f"- {memory.memory} "
            f"({memory.category}, "
            f"Importance: {memory.importance})\n"
        )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=memory_text,
        config=types.GenerateContentConfig(
            system_instruction=prompt,
            response_mime_type="application/json",
        ),
    )

    return json.loads(response.text)