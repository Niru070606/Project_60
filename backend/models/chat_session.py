from database import db


class ChatSession(db.Model):
    __tablename__ = "chat_sessions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    conversation_id = db.Column(
        db.Integer,
        db.ForeignKey("conversations.id"),
        nullable=False
    )
    
    summary = db.Column(
        db.Text,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    conversation = db.relationship(
        "Conversation",
        back_populates="sessions"
    )

    messages = db.relationship(
        "Message",
        back_populates="chat_session",
        lazy=True,
        cascade="all, delete-orphan"
    )