import json

from services.memory.embedding_service import (
    create_embedding,
    MODEL,
)

from repositories.memory_embedding_repository import (
    update_embedding,
)


def sync_memory_embedding(memory):

    embedding = create_embedding(
        memory.memory
    )

    embedding_json = json.dumps(
        embedding
    )

    return update_embedding(
        memory_id=memory.id,
        model=MODEL,
        embedding=embedding_json,
    )