from services.chat_service import client
from google.genai import types
import json

from services.session_summary_prompt import build_summary_prompt

def summarize_session(messages):

    prompt = build_summary_prompt()

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