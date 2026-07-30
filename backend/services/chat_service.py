from google import genai
from google.genai import types

from config import Config
from services.brain.builder import build_brain


client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)


def send_message(message: str) -> str:

    brain = build_brain(message)

    print("Intent:", brain.intent)

    history = brain.history

    contents = history

    if contents:
        contents += "\n"

    contents += f"user: {message}"

    # print("\n================ SYSTEM PROMPT ================\n")
    # print(brain["system_prompt"])
    # print("\n==============================================\n")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=brain.system_prompt,
        ),
        contents=contents,
    )

    return response.text