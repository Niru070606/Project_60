from database import db
from models.mood import MoodState, MoodHistory
from repositories.conversation_repository import get_or_create_conversation
from datetime import datetime


def get_or_create_mood_state():
    conversation = get_or_create_conversation()

    mood_state = MoodState.query.filter_by(conversation_id=conversation.id).first()

    if mood_state is None:
        mood_state = MoodState(conversation_id=conversation.id)
        db.session.add(mood_state)
        db.session.commit()

    return mood_state


def get_mood_state():
    return get_or_create_mood_state()


def save_mood_state(
    mood: str = None,
    intensity: int = None,
    cooldown_until: datetime = None,
    reason: str = None,
    trigger_message: str = None,
):
    mood_state = get_or_create_mood_state()

    changed = False

    if mood is not None:
        mood_state.current_mood = mood
        changed = True

    if intensity is not None:
        mood_state.intensity = intensity
        changed = True

    if cooldown_until is not None:
        mood_state.cooldown_until = cooldown_until
        changed = True

    if changed:
        mood_state.last_mood_change = datetime.utcnow()

        history = MoodHistory(
            mood_state_id=mood_state.id,
            mood=mood_state.current_mood,
            intensity=mood_state.intensity,
            reason=reason,
            trigger_message=trigger_message,
        )
        db.session.add(history)

        db.session.commit()

    return mood_state


def reset_mood_state():
    mood_state = get_or_create_mood_state()

    mood_state.current_mood = "calm"
    mood_state.intensity = mood_state.baseline_intensity
    mood_state.cooldown_until = None
    mood_state.enable_mood_system = True
    mood_state.last_mood_change = datetime.utcnow()

    history = MoodHistory(
        mood_state_id=mood_state.id,
        mood="calm",
        intensity=mood_state.baseline_intensity,
        reason="Reset to baseline",
    )
    db.session.add(history)

    db.session.commit()

    return mood_state


def set_mood_enabled(enabled: bool):
    mood_state = get_or_create_mood_state()

    mood_state.enable_mood_system = enabled
    db.session.commit()

    return mood_state


def get_mood_history(limit: int = 10):
    mood_state = get_or_create_mood_state()

    return (
        MoodHistory.query.filter_by(mood_state_id=mood_state.id)
        .order_by(MoodHistory.timestamp.desc())
        .limit(limit)
        .all()
    )


def is_mood_cooldown_active(mood_state: MoodState) -> bool:
    if mood_state.cooldown_until is None:
        return False

    return datetime.utcnow() < mood_state.cooldown_until


def get_mood_state_for_response():
    mood_state = get_mood_state()

    return {
        "current_mood": mood_state.current_mood,
        "intensity": mood_state.intensity,
        "enable_mood_system": mood_state.enable_mood_system,
        "cooldown_active": is_mood_cooldown_active(mood_state),
    }