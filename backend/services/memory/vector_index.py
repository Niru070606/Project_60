from repositories.memory_embedding_repository import (
    get_all_embeddings,
)


def get_candidate_embeddings():
    """
    Returns embeddings that semantic search
    should compare against.

    Currently loads all embeddings.

    Later this will use:
    - FAISS
    - ChromaDB
    - pgvector
    - Pinecone
    without changing Semantic Search.
    """

    return get_all_embeddings()