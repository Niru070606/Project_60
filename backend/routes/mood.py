from flask import Blueprint, jsonify, request

from repositories.mood_repository import (
    get_mood_state,
    reset_mood_state,
    set_mood_enabled,
    get_mood_state_for_response,
    get_mood_history,
)

from services.mood_engine import MoodEngine, build_mood_prompt

mood_bp = Blueprint("mood", __name__)


@mood_bp.route("/mood", methods=["GET"])
def get_mood():
    mood_data = get_mood_state_for_response()

    mood_state = get_mood_state()

    history = get_mood_history(limit=10)

    return jsonify({
        "current_mood": mood_data["current_mood"],
        "intensity": mood_data["intensity"],
        "enable_mood_system": mood_state.enable_mood_system,
        "baseline_intensity": mood_state.baseline_intensity,
        "cooldown_active": mood_data["cooldown_active"],
        "cooldown_until": (
            mood_state.cooldown_until.isoformat()
            if mood_state.cooldown_until else None
        ),
        "mood_history": [
            {
                "mood": h.mood,
                "intensity": h.intensity,
                "reason": h.reason,
                "timestamp": h.timestamp.strftime("%B %d, %Y %I:%M %p")
                if h.timestamp else None,
            }
            for h in history
        ],
    })


@mood_bp.route("/mood/settings", methods=["PUT"])
def update_mood_settings():
    data = request.json or {}

    mood_state = get_mood_state()

    if "enable_mood_system" in data:
        set_mood_enabled(data["enable_mood_system"])

    if "baseline_intensity" in data:
        mood_state.baseline_intensity = data["baseline_intensity"]

    if "reset_to_baseline" in data and data["reset_to_baseline"]:
        reset_mood_state()

    from database import db
    db.session.commit()

    updated_state = get_mood_state()

    return jsonify({
        "success": True,
        "current_mood": updated_state.current_mood,
        "intensity": updated_state.intensity,
        "enable_mood_system": updated_state.enable_mood_system,
    })


@mood_bp.route("/mood/reset", methods=["POST"])
def reset_mood():
    reset_mood_state()

    mood_state = get_mood_state()

    return jsonify({
        "success": True,
        "message": "Mood reset to baseline (calm)",
        "current_mood": mood_state.current_mood,
        "intensity": mood_state.baseline_intensity,
    })


@mood_bp.route("/mood/expression", methods=["GET"])
def get_mood_expression():
    mood_data = get_mood_state_for_response()

    from services.personality_service import get_personality
    personality = get_personality()

    engine = MoodEngine(personality=personality)

    expression_payload = engine.evaluate_for_response()

    mood_prompt = build_mood_prompt(expression_payload)

    return jsonify({
        "mood": expression_payload,
        "prompt": mood_prompt,
    })