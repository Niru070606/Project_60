from repositories.memory_entity_repository import (
    create_memory_entity,
    find_memory_entity,
    get_entities_for_memory,
    get_memories_for_entity,
    get_memory_records_for_entity,
)

from repositories.transaction_repository import (
    flush,
    commit,
    rollback,
)


def link_memory_to_entity(
    memory_id: int,
    entity_id: int,
):

    existing = find_memory_entity(
        memory_id,
        entity_id,
    )

    if existing:
        return existing

    try:

        association = create_memory_entity(
            memory_id,
            entity_id,
        )

        flush()
        commit()

        return association

    except Exception:

        rollback()

        raise

def link_memory_to_entities(
    memory_id: int,
    entity_ids: list[int],
):
    links = []

    for entity_id in entity_ids:

        link = link_memory_to_entity(
            memory_id,
            entity_id,
        )

        links.append(link)

    return links

def get_memory_entities(
    memory_id: int,
):
    return get_entities_for_memory(
        memory_id
    )

def link_memory_to_resolved_entities(
    memory_id: int,
    entities,
):
    entity_ids = [
        entity.id
        for entity in entities
    ]

    return link_memory_to_entities(
        memory_id,
        entity_ids,
    )

def get_entity_memories(
    entity_id: int,
):
    return get_memories_for_entity(
        entity_id
    )

def get_entity_memory_records(
    entity_id: int,
):
    return get_memory_records_for_entity(
        entity_id
    )

def get_memories_for_entities(
    entity_ids: list[int],
):
    memories = {}

    for entity_id in entity_ids:

        entity_memories = get_entity_memory_records(
            entity_id
        )

        for memory in entity_memories:
            memories[memory.id] = memory

    return list(memories.values())