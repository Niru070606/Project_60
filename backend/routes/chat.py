from flask import Blueprint, request, jsonify

from services.chat_service import (
    send_message,
    reset_chat
)

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():

    data = request.json

    user_message = data["message"]

    reply = send_message(user_message)

    return jsonify({
        "reply": reply
    })


@chat_bp.route("/chat/reset", methods=["POST"])
def reset():

    reset_chat()

    return jsonify({
        "success": True
    })