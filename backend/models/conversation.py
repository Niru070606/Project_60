from database import db


class Conversation(db.Model):
    __tablename__ = "conversations"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    sessions = db.relationship(
        "ChatSession",
        back_populates="conversation",
        lazy=True,
        cascade="all, delete-orphan"
    )

    memories = db.relationship(
        "Memory",
        backref="conversation",
        lazy=True,
        cascade="all, delete-orphan"
    )