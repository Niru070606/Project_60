from flask import Blueprint, jsonify
from datetime import datetime
from collections import Counter

from database import db
from models.memory import Memory
from models.message import Message
from models.chat_session import ChatSession
from models.conversation import Conversation
from models.entity import Entity
from models.memory_entity import MemoryEntity

analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/analytics/memory-overview", methods=["GET"])
def get_memory_overview():
    """Get overall memory statistics."""

    total_memories = Memory.query.count()

    conversations = Conversation.query.all()
    total_added = total_memories

    merged_count = Memory.query.filter_by(reflected=True).count()

    total_entities = len(Entity.query.distinct(Entity.name).all())

    return jsonify({
        "total_memories": total_memories,
        "memories_added": total_added,
        "memories_merged": merged_count,
        "total_entities": total_entities,
    })


@analytics_bp.route("/analytics/memory-growth", methods=["GET"])
def get_memory_growth():
    """Get memory growth over time."""

    memories = Memory.query.order_by(Memory.created_at.asc()).all()

    daily_counts = Counter()
    for memory in memories:
        date_key = memory.created_at.strftime("%Y-%m-%d")
        daily_counts[date_key] += 1

    sorted_dates = sorted(daily_counts.keys())

    return jsonify({
        "growth_data": [
            {"date": date, "count": daily_counts[date]}
            for date in sorted_dates[-30:]
        ],
        "total_growth": len(memories),
    })


@analytics_bp.route("/analytics/memory-categories", methods=["GET"])
def get_memory_categories():
    """Get memory categories breakdown."""

    categories = db.session.query(
        Memory.category,
        db.func.count(Memory.id).label('count')
    ).group_by(Memory.category).all()

    return jsonify({
        "categories": [
            {"category": cat[0], "count": cat[1]}
            for cat in categories
        ]
    })


@analytics_bp.route("/analytics/entities", methods=["GET"])
def get_entities():
    """Get entities with usage stats."""

    entity_query = db.session.query(
        Entity.name,
        Entity.entity_type,
        db.func.count(MemoryEntity.entity_id).label('memory_count')
    ).join(
        MemoryEntity, Entity.id == MemoryEntity.entity_id
    ).group_by(Entity.id, Entity.name, Entity.entity_type).order_by(
        db.func.count(MemoryEntity.entity_id).desc()
    ).limit(10).all()

    return jsonify({
        "entities": [
            {
                "name": eq[0],
                "type": eq[1],
                "memory_count": eq[2]
            }
            for eq in entity_query
        ]
    })


@analytics_bp.route("/analytics/retrieval-stats", methods=["GET"])
def get_retrieval_stats():
    """Get memory retrieval statistics."""

    memories = Memory.query.all()

    total_retrievals = sum(m.retrieval_count for m in memories)

    if memories:
        avg_retrieval = total_retrievals / len(memories)
        top_retrieved = Memory.query.order_by(
            Memory.retrieval_count.desc()
        ).limit(5).all()

        retrieval_activity = Counter()
        for memory in memories:
            date_key = memory.created_at.strftime("%Y-%m-%d")
            retrieval_activity[date_key] += memory.retrieval_count
    else:
        avg_retrieval = 0
        top_retrieved = []
        retrieval_activity = Counter()

    return jsonify({
        "total_retrievals": total_retrievals,
        "average_retrieval_score": round(avg_retrieval, 2),
        "top_retrieved": [
            {
                "id": m.id,
                "text": m.memory[:100],
                "retrieval_count": m.retrieval_count
            }
            for m in top_retrieved
        ],
        "retrieval_activity": [
            {"date": date, "count": count}
            for date, count in sorted(retrieval_activity.items())[-30:]
        ]
    })


@analytics_bp.route("/analytics/chat-usage", methods=["GET"])
def get_chat_usage():
    """Get chat usage statistics."""

    total_messages = Message.query.count()

    conversations = Conversation.query.all()
    total_conversations = len(conversations)

    sessions = ChatSession.query.all()
    total_sessions = len(sessions)

    if sessions:
        messages_per_session = [
            len(session.messages) for session in sessions
        ]
        avg_messages = sum(messages_per_session) / len(messages_per_session)
    else:
        avg_messages = 0

    daily_activity = Counter()
    for session in sessions:
        date_key = session.created_at.strftime("%Y-%m-%d")
        daily_activity[date_key] += len(session.messages)

    return jsonify({
        "total_conversations": total_conversations,
        "total_messages": total_messages,
        "total_sessions": total_sessions,
        "average_messages_per_session": round(avg_messages, 2),
        "activity_over_time": [
            {"date": date, "count": count}
            for date, count in sorted(daily_activity.items())[-30:]
        ]
    })


@analytics_bp.route("/analytics/summary", methods=["GET"])
def get_analytics_summary():
    """Get a complete analytics summary."""

    memories = Memory.query.all()
    messages = Message.query.all()
    conversations = Conversation.query.all()

    memory_count = len(memories)
    chat_count = len(messages)
    entity_count = len(Entity.query.distinct(Entity.name).all())

    if memories:
        categories = db.session.query(
            Memory.category,
            db.func.count(Memory.id).label('count')
        ).group_by(Memory.category).all()
    else:
        categories = []

    if conversations:
        first_conv = conversations[0]
        created_date = first_conv.created_at.strftime("%Y-%m-%d")
    else:
        created_date = None

    return jsonify({
        "memory_count": memory_count,
        "chat_count": chat_count,
        "entity_count": entity_count,
        "categories": [
            {"category": cat[0], "count": cat[1]}
            for cat in categories
        ],
        "created_date": created_date
    })