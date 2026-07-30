from google.genai import types

from repositories.conversation_repository import get_or_create_conversation
from repositories.chat_session_repository import get_latest_session
from repositories.message_repository import get_messages


def get_recent_messages(limit=300):
    conversation = get_or_create_conversation()

    session = get_latest_session(conversation.id)

    if session is None:
        return []

    messages = get_messages(session.id)

    return messages[-limit:]