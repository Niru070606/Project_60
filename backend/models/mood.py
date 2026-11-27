from database import db
from datetime import datetime


class MoodState(db.Model):
    __tablename__ = "mood_states"

    id = db.Column(db.Integer, primary_key=True)

    conversation_id = db.Column(
        db.Integer,
        db.ForeignKey("conversations.id"),
        nullable=False,
        unique=True,
    )

    current_mood = db.Column(db.String(50), nullable=False, default="calm")

    intensity = db.Column(db.Integer, nullable=False, default=50)

    baseline_intensity = db.Column(db.Integer, nullable=False, default=50)

    enable_mood_system = db.Column(db.Boolean, nullable=False, default=True)

    cooldown_until = db.Column(db.DateTime, nullable=True)

    last_mood_change = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    last_updated = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    mood_history = db.relationship("MoodHistory", backref="mood_state", lazy=True, cascade="all, delete-orphan")

    conversation = db.relationship("Conversation", backref="mood_state")


class MoodHistory(db.Model):
    __tablename__ = "mood_history"

    id = db.Column(db.Integer, primary_key=True)

    mood_state_id = db.Column(
        db.Integer,
        db.ForeignKey("mood_states.id"),
        nullable=False,
    )

    mood = db.Column(db.String(50), nullable=False)

    intensity = db.Column(db.Integer, nullable=False)

    trigger_message = db.Column(db.Text, nullable=True)

    reason = db.Column(db.Text, nullable=True)

    timestamp = db.Column(db.DateTime, server_default=db.func.now())