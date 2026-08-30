import json

from services.memory.embedding_service import create_embedding
from repositories.memory_embedding_repository import (
    get_embedding_by_memory_id,
    get_all_embeddings,
)

from repositories.memory_repository import (
    get_memory_by_id,
)


def find_related_memories(
    memory,
    threshold: float = 0.85,
    limit: int = 10,
):
    """
    Finds memories that are semantically
    similar to the given memory.

    Detection only.
    Does not modify the database.
    """

    target_embedding_record = (
        get_embedding_by_memory_id(
            memory.id
        )
    )

    if not target_embedding_record:
        return []

    target_embedding = json.loads(
        target_embedding_record.embedding
    )

    embeddings = get_all_embeddings()

    results = []

    for embedding in embeddings:

        # Don't compare the memory with itself.
        if embedding.memory_id == memory.id:
            continue

        stored_embedding = json.loads(
            embedding.embedding
        )

        score = cosine_similarity(
            target_embedding,
            stored_embedding,
        )

        if score >= threshold:

            related_memory = get_memory_by_id(
                embedding.memory_id
            )

            if related_memory:
                results.append(
                    (
                        related_memory,
                        score,
                    )
                )

    results.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    return results[:limit]


def cosine_similarity(
    vector1: list[float],
    vector2: list[float],
):

    dot_product = sum(
        a * b
        for a, b in zip(vector1, vector2)
    )

    magnitude1 = (
        sum(a * a for a in vector1)
        ** 0.5
    )

    magnitude2 = (
        sum(b * b for b in vector2)
        ** 0.5
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (
        magnitude1 * magnitude2
    )