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

        SIMILARITY_THRESHOLD = 0.60

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

def find_semantically_similar_memory(
    memory_text: str,
    limit: int = 5,
    threshold: float = 0.75,
):
    """
    Finds existing memories that are
    semantically similar to the supplied memory.
    """

    memory_embedding = create_embedding(
        memory_text
    )

    embeddings = get_candidate_embeddings()

    results = []

    for embedding in embeddings:

        stored_embedding = json.loads(
            embedding.embedding
        )

        score = cosine_similarity(
            memory_embedding,
            stored_embedding,
        )

        if score >= threshold:

            memory = get_memory_by_id(
                embedding.memory_id
            )

            if memory:

                results.append(
                    (
                        memory,
                        score,
                    )
                )

    results.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    return results[:limit]