from services.reflection.reflection_scheduler import (
    process_reflection,
)

from repositories.conversation_repository import get_or_create_conversation
from repositories.chat_session_repository import (
    create_session,
    get_latest_session,
    update_summary
)
from repositories.message_repository import (save_message, get_messages)
from repositories.mood_repository import get_mood_state_for_response
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

from services.personality_service import get_personality
from services.mood_engine import MoodEngine

def chat(message: str) -> str:

    conversation = get_or_create_conversation()

    session = get_latest_session(
        conversation.id
    )

    if session is None:
        session = create_session(
            conversation.id
        )

    save_message(
        chat_session_id=session.id,
        sender="user",
        message=message,
    )

    personality = get_personality()
    mood_engine = MoodEngine(personality=personality)

    current_state = get_mood_state_for_response()
    mood_engine.evaluate_mood(message, current_state)

    reply = send_message(
        message
    )

    save_message(
        chat_session_id=session.id,
        sender="ai",
        message=reply,
    )

    reinforce_relationship()

    messages = get_messages(
        session.id
    )

    user_message_count = sum(
        1
        for msg in messages
        if msg.sender == "user"
    )

    print("User message count:", user_message_count)

    process_reflection(
        user_message_count
    )

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

    from repositories.mood_repository import get_mood_state, reset_mood_state

    mood_state = get_mood_state()

    if mood_state.current_mood != "calm":
        reset_mood_state()

    create_session(conversation.id)

def get_current_messages():

    conversation = get_or_create_conversation()

    session = get_latest_session(conversation.id)

    if session is None:
        return []

    return get_messages(session.id)