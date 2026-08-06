import json

from services.memory.embedding_service import (
    create_embedding,
)

from services.memory.similarity import (
    cosine_similarity,
)

from services.memory.vector_index import (
    get_candidate_embeddings,
)

from repositories.memory_repository import (
    get_memory_by_id,
)

def semantic_search(
    user_message: str,
    limit: int = 5,
):
    """
    Returns the most semantically
    similar memories.
    """

    user_embedding = create_embedding(
        user_message
    )

    embeddings = get_candidate_embeddings()

    results = []

    for embedding in embeddings:

        stored_embedding = json.loads(
            embedding.embedding
        )

        score = cosine_similarity(
            user_embedding,
            stored_embedding,
        )

        SIMILARITY_THRESHOLD = 0.75

        if score >= SIMILARITY_THRESHOLD:

            results.append(
                (
                    embedding,
                    score,
                )
            )
            
    results.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    top_memories = []

    for embedding, score in results[:limit]:

        memory = get_memory_by_id(
            embedding.memory_id
        )

        if memory:

            top_memories.append(
                (
                    memory,
                    score,
                )
            )

    return top_memories