from database import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    chat_session_id = db.Column(
        db.Integer,
        db.ForeignKey("chat_sessions.id"),
        nullable=False
    )

    sender = db.Column(
        db.String(20),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    chat_session = db.relationship(
        "ChatSession",
        back_populates="messages"
    )