from repositories.conversation_repository import get_or_create_conversation
from repositories.chat_session_repository import (
    create_session,
    get_latest_session,
    update_summary
)
from repositories.message_repository import (save_message, get_messages)
from services.chat_service import send_message

from services.session_summary_service import summarize_session
from services.memory_service import save_extracted_memories

from services.relationship_service import reinforce_relationship

from services.relationship_reflection_service import (
    reflect_relationship,
)

from services.relationship_service import (
    apply_relationship_changes,
)

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

    reinforce_relationship()

    return reply

def start_new_session():

    conversation = get_or_create_conversation()

    current_session = get_latest_session(conversation.id)

    if current_session:

        messages = get_messages(current_session.id)

        if messages:

            reflection = summarize_session(messages)

            update_summary(
                current_session,
                reflection["summary"],
            )

            save_extracted_memories(
                reflection["memories"],
            )

            relationship_changes = reflect_relationship(messages)

            apply_relationship_changes(relationship_changes)

    create_session(conversation.id)

def get_current_messages():

    conversation = get_or_create_conversation()

    session = get_latest_session(conversation.id)

    if session is None:
        return []

    return get_messages(session.id)