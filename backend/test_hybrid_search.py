from app import app

from services.memory.hybrid_search import hybrid_search


with app.app_context():

    query = "What school am I studying at?"

    results = hybrid_search(
        query,
        limit=5,
    )

    print("\n===== HYBRID SEARCH TEST =====")
    print("Query:", query)
    print()

    for memory in results:

        print(
            f"Memory ID: {memory.id} | "
            f"Memory: {memory.memory}"
        )

    print("==============================")