from flask import Blueprint, request, jsonify

from services.conversation_service import chat, start_new_session
from services.chat_service import reset_chat

from services.conversation_service import (
    chat,
    start_new_session,
    get_current_messages,
)

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["POST"])
def send_chat():

    data = request.json

    user_message = data["message"]

    reply = chat(user_message)

    return jsonify({
        "reply": reply
    })


@chat_bp.route("/chat/reset", methods=["POST"])
def reset():

    start_new_session()

    return jsonify({
        "success": True
    })

@chat_bp.route("/messages", methods=["GET"])
def messages():

    messages = get_current_messages()

    return jsonify([
        {
            "id": msg.id,
            "sender": msg.sender,
            "message": msg.message,
            "time": msg.created_at.strftime("%I:%M %p"),
        }
        for msg in messages
    ])