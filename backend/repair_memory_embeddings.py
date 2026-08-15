from app import app

from services.memory_service import create_missing_embedding
from repositories.memory_repository import get_memories
from repositories.memory_embedding_repository import (
    get_embedding_by_memory_id,
)
from repositories.conversation_repository import (
    get_or_create_conversation,
)

with app.app_context():

    conversation = get_or_create_conversation()

    memories = get_memories(
        conversation.id
    )

    for memory in memories:

        embedding = get_embedding_by_memory_id(
            memory.id
        )

        if embedding:
            continue

        print(
            "🔥 Missing embedding:",
            memory.id,
            memory.memory
        )

        create_missing_embedding(memory)

        print(
            "✅ Embedding created:",
            memory.id
        )