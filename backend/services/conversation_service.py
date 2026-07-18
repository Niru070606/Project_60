from repositories.conversation_repository import get_or_create_conversation
from repositories.chat_session_repository import (
    create_session,
    get_latest_session,
)
from repositories.message_repository import (save_message, get_messages)
from services.chat_service import send_message

def chat(message: str) -> str:

    conversation = get_or_create_conversation()

    session = get_latest_session(conversation.id)

    if session is None:
        session = create_session(conversation.id)

    save_message(
        chat_session_id=session.id,
        sender="user",
        message=message,
    )

    reply = send_message(message)

    save_message(
        chat_session_id=session.id,
        sender="ai",
        message=reply,
    )

    return reply

def start_new_session():
    conversation = get_or_create_conversation()

    create_session(conversation.id)

def get_current_messages():

    conversation = get_or_create_conversation()

    session = get_latest_session(conversation.id)

    if session is None:
        return []

    return get_messages(session.id)