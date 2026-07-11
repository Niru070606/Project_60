from google import genai
from google.genai import types

from config import Config
from services.personality_service import get_system_prompt

client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=get_system_prompt()
    )
)

def generate_reply(message):
    response = chat.send_message(message)
    return response.text