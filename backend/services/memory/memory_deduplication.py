import json

from services.memory.embedding_service import create_embedding
from services.memory.similarity import cosine_similarity

from repositories.memory_embedding_repository import (
    get_embeddings_by_conversation,
)

from repositories.memory_repository import (
    get_memory_by_id,
)


DEDUPLICATION_THRESHOLD = 0.85


def find_semantic_duplicate(
    conversation_id: int,
    new_memory: str,
):

    new_embedding = create_embedding(
        new_memory
    )

    embeddings = get_embeddings_by_conversation(
        conversation_id
    )

    best_memory = None
    best_score = 0.0

    for embedding in embeddings:

        stored_embedding = json.loads(
            embedding.embedding
        )

        score = cosine_similarity(
            new_embedding,
            stored_embedding,
        )

        if score > best_score:

            best_score = score

            best_memory = get_memory_by_id(
                embedding.memory_id
            )

    print("\n===== MEMORY DEDUPLICATION =====")
    print("New:", new_memory)
    print("Best Score:", best_score)

    if best_memory:
        print("Best Match:", best_memory.memory)
    else:
        print("Best Match: None")

    print("================================")

    if best_score >= DEDUPLICATION_THRESHOLD:

        return best_memory

    return None