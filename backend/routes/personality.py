from flask import Blueprint, request, jsonify

from services.personality_service import (
    save_personality,
    get_personality,
)

personality_bp = Blueprint("personality", __name__)

@personality_bp.route("/personality", methods=["POST"])
def update_personality():

    personality = request.json

    save_personality(personality)

    return jsonify({
        "success": True,
        "message": "Personality updated."
    })


@personality_bp.route("/personality", methods=["GET"])
def personality():

    return jsonify(get_personality())