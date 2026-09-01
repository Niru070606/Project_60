from repositories.entity_repository import (
    find_entity_by_name,
    create_entity,
)

from repositories.transaction_repository import (
    flush,
    commit,
    rollback,
)


def resolve_entity(
    name: str,
    entity_type: str,
):

    existing = find_entity_by_name(
        name,
        entity_type,
    )

    if existing:
        return existing

    try:

        entity = create_entity(
            name=name,
            entity_type=entity_type,
        )

        flush()
        commit()

        return entity

    except Exception:

        rollback()

        raise

def resolve_entities(
    entities: list[dict],
):
    resolved = []

    for entity in entities:

        resolved_entity = resolve_entity(
            name=entity["text"],
            entity_type=entity["type"],
        )

        resolved.append(
            resolved_entity
        )

    return resolved