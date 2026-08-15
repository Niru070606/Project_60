from repositories.memory_repository import (
    find_similar_memory,
)


def validate_reflections(
    reflections,
    conversation_id,
):
    if not isinstance(reflections, list):
        return []

    valid = []

    for reflection in reflections:

        if not isinstance(reflection, dict):
            continue

        memory = reflection.get("memory")
        category = reflection.get("category")
        importance = reflection.get("importance")

        if not memory:
            continue

        if not category:
            continue

        if not isinstance(importance, int):
            continue

        importance = max(
            1,
            min(importance, 100)
        )

        existing = find_similar_memory(
            conversation_id,
            memory,
        )

        if existing:
            continue

        valid.append({
            "memory": memory.strip(),
            "category": category.strip(),
            "importance": importance,
        })

    return valid