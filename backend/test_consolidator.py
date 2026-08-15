from app import app

from repositories.conversation_repository import (
    get_or_create_conversation,
)

from services.reflection.memory_consolidator import (
    consolidate_memory,
)


with app.app_context():

    conversation = get_or_create_conversation()

    reflection = {
        "memory": "Neil named the AI 'Jeycel' after a girl who inspired him..",
        "category": "Personals",
        "importance": 95,
    }

    result = consolidate_memory(
        reflection,
        conversation.id,
    )

    print("\n===== Consolidation Result =====")
    print("Action:", result["action"])
    print("Memory:", result["memory"])