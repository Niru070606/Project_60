from app import app

from services.memory.hybrid_search import (
    hybrid_search,
)


with app.app_context():

    print("\n===== HYBRID ENTITY SEARCH TEST =====")

    user_message = (
    "Tell me about Project Lecyrus."
)

    print(
        "User message:",
        user_message,
    )

    results = hybrid_search(
        user_message=user_message,
        limit=5,
    )

    print("\n===== FINAL RESULTS =====")

    for memory in results:

        print(
            "Memory:",
            memory.id,
            "|",
            memory.memory,
        )

    print("=========================")