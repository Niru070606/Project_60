from flask import Blueprint, jsonify

from models.memory import Memory
from services.memory_service import remove_memory

memory_bp = Blueprint("memory", __name__)

@memory_bp.route("/memories", methods=["GET"])
def get_all_memories():

    memories = Memory.query.order_by(
        Memory.importance.desc()
    ).all()

    return jsonify([
        {
            "id": memory.id,
            "memory": memory.memory,
            "category": memory.category,
            "importance": memory.importance,
            "retrieval_count": memory.retrieval_count,
            "created_at": memory.created_at.strftime("%B %d, %Y"),
        }
        for memory in memories
    ])


@memory_bp.route("/memories/<int:memory_id>", methods=["DELETE"])
def delete(memory_id):

    memory = Memory.query.get(memory_id)

    if memory is None:
        return jsonify({
            "error": "Memory not found"
        }), 404

    remove_memory(memory)

    return jsonify({
        "success": True
    })

