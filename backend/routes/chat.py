from flask import Blueprint, request, jsonify
from services.ai_service import generate_reply

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():

    data = request.json

    message = data["message"]

    reply = generate_reply(message)

    return jsonify({
        "reply": reply
    })