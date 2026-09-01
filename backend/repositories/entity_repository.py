from models.entity import Entity
from database import db


def get_entities():
    return Entity.query.all()


def get_entity_by_id(entity_id: int):
    return Entity.query.get(entity_id)


def find_entity_by_name(
    name: str,
    entity_type: str | None = None,
):

    query = Entity.query.filter(
        db.func.lower(Entity.name)
        == name.lower()
    )

    if entity_type:
        query = query.filter(
            Entity.entity_type
            == entity_type
        )

    return query.first()


def create_entity(
    name: str,
    entity_type: str,
):

    entity = Entity(
        name=name,
        entity_type=entity_type,
    )

    db.session.add(entity)

    return entity