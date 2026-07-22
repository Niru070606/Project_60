from google import genai
from google.genai import types

from config import Config
from services.personality_service import get_personality
from services.prompt_builder import build_system_prompt

from services.memory_service import load_memories


client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)

chat = None


def start_chat():
    """Starts a new Gemini chat using the current personality."""

    global chat

    personality = get_personality()

    memories = load_memories()

    prompt = build_system_prompt(
        personality,
        memories,
    )

    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=prompt
        )
    )


def send_message(message: str) -> str:
    """Sends a message to the active chat."""

    global chat

    if chat is None:
        start_chat()

    response = chat.send_message(message)

    return response.text


def reset_chat():
    """Starts a fresh conversation."""

    start_chat()