from database import db
from models.memory import Memory


def save_memory(
    conversation_id: int,
    memory: str,
    category: str,
    importance: int,
):
    mem = Memory(
        conversation_id=conversation_id,
        memory=memory,
        category=category,
        importance=importance,
    )

    db.session.add(mem)
    db.session.commit()

    return mem


def get_memories(
    conversation_id: int,
    limit: int | None = None,
):

    query = (
        Memory.query
        .filter_by(conversation_id=conversation_id)
        .order_by(Memory.importance.desc())
    )

    if limit:
        query = query.limit(limit)

    return query.all()


def delete_memory(memory: Memory):
    db.session.delete(memory)
    db.session.commit()

def find_memory(
    conversation_id: int,
    memory: str,
):
    return (
        Memory.query
        .filter_by(
            conversation_id=conversation_id,
            memory=memory,
        )
        .first()
    )

def update_importance(
    memory: Memory,
    importance: int,
):
    memory.importance = max(
        memory.importance,
        importance,
    )

    db.session.commit()