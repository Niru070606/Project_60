from database import db
from models.memory_embedding import MemoryEmbedding


def save_embedding(
    memory_id: int,
    model: str,
    embedding: str,
):

    memory_embedding = MemoryEmbedding(
        memory_id=memory_id,
        model=model,
        embedding=embedding,
    )

    db.session.add(memory_embedding)

    return memory_embedding


def get_all_embeddings():

    return (
        MemoryEmbedding.query
        .all()
    )