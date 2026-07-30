import json

from google.genai import types

from services.chat_service import client
from services.prompts.relationship_reflection_prompt import (
    build_relationship_reflection_prompt,
)


def reflect_relationship(messages):

    prompt = build_relationship_reflection_prompt()

    conversation = ""

    for msg in messages:
        conversation += f"{msg.sender}: {msg.message}\n"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation,
        config=types.GenerateContentConfig(
            system_instruction=prompt,
            response_mime_type="application/json",
        ),
    )

    return json.loads(response.text)