from database import db
from models.chat_session import ChatSession


def create_session(conversation_id: int):
    session = ChatSession(
        conversation_id=conversation_id
    )

    db.session.add(session)
    db.session.commit()

    return session


def get_latest_session(conversation_id: int):
    return (
        ChatSession.query
        .filter_by(conversation_id=conversation_id)
        .order_by(ChatSession.id.desc())
        .first()
    )

def update_summary(session: ChatSession,summary: str,):
    session.summary = summary

    db.session.commit()