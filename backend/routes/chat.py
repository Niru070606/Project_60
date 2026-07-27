from flask import Blueprint, request, jsonify


from services.conversation_service import (
    chat,
    start_new_session,
    get_current_messages,
)

from services.session_summary_service import summarize_session
from repositories.chat_session_repository import get_latest_session
from repositories.message_repository import get_messages
from repositories.conversation_repository import get_or_create_conversation




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

@chat_bp.route("/chat/test-summary", methods=["GET"])
def test_summary():

    conversation = get_or_create_conversation()

    session = get_latest_session(conversation.id)

    messages = get_messages(session.id)

    result = summarize_session(messages)

    return jsonify(result)