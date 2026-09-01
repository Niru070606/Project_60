from database import db
from models.memory_embedding import MemoryEmbedding
from models.memory import Memory


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

    print(
    "🔥 SAVING EMBEDDING:",
    memory_id,
    model,
    len(embedding)
    )
    db.session.commit()

    return memory_embedding


def get_all_embeddings():

    return (
        MemoryEmbedding.query
        .all()
    )

def get_embeddings_by_conversation(
    conversation_id: int,
):
    return (
        MemoryEmbedding.query
        .join(
            Memory,
            Memory.id == MemoryEmbedding.memory_id
        )
        .filter(
            Memory.conversation_id == conversation_id
        )
        .all()
    )

def get_embedding_by_memory_id(
    memory_id: int,
):
    return (
        MemoryEmbedding.query
        .filter_by(
            memory_id=memory_id
        )
        .first()
    )


def update_embedding(
    memory_id: int,
    model: str,
    embedding: str,
):

    memory_embedding = get_embedding_by_memory_id(
        memory_id
    )

    if memory_embedding is None:

        return save_embedding(
            memory_id=memory_id,
            model=model,
            embedding=embedding,
        )

    memory_embedding.model = model
    memory_embedding.embedding = embedding

    db.session.commit()

    return memory_embedding