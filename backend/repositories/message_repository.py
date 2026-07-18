from database import db
from models.message import Message


def save_message(
    chat_session_id: int,
    sender: str,
    message: str,
):
    msg = Message(
        chat_session_id=chat_session_id,
        sender=sender,
        message=message,
    )

    db.session.add(msg)
    db.session.commit()

    return msg


def get_messages(chat_session_id: int):
    return (
        Message.query
        .filter_by(chat_session_id=chat_session_id)
        .order_by(Message.created_at.asc())
        .all()
    )