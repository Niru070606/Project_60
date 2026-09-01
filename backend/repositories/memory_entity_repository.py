from models.memory_entity import MemoryEntity
from database import db


def create_memory_entity(
    memory_id: int,
    entity_id: int,
):
    association = MemoryEntity(
        memory_id=memory_id,
        entity_id=entity_id,
    )

    db.session.add(association)

    return association


def find_memory_entity(
    memory_id: int,
    entity_id: int,
):
    return MemoryEntity.query.filter_by(
        memory_id=memory_id,
        entity_id=entity_id,
    ).first()


def get_entities_for_memory(
    memory_id: int,
):
    return (
        MemoryEntity.query
        .filter_by(
            memory_id=memory_id
        )
        .all()
    )


def get_memories_for_entity(
    entity_id: int,
):
    return (
        MemoryEntity.query
        .filter_by(
            entity_id=entity_id
        )
        .all()
    )


def delete_memory_entity(
    memory_id: int,
    entity_id: int,
):
    association = find_memory_entity(
        memory_id,
        entity_id,
    )

    if association:
        db.session.delete(
            association
        )

    return association

def get_memory_records_for_entity(
    entity_id: int,
):
    links = get_memories_for_entity(
        entity_id
    )

    return [
        link.memory
        for link in links
    ]