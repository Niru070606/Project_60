import json

from google import genai
from google.genai import types

from config import Config

from services.prompts.reflection_prompt import (
    build_reflection_prompt,
)

client = genai.Client(
    api_key=Config.GEMINI_API_KEY,
)


def reflect(memories):

    memory_text = "\n".join(
        f"- {memory.memory}"
        for memory in memories
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=build_reflection_prompt(),
        ),
        contents=memory_text,
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.removeprefix("```json").removesuffix("```").strip()

    elif text.startswith("```"):
        text = text.removeprefix("```").removesuffix("```").strip()

    return json.loads(text)