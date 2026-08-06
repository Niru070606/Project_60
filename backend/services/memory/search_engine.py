from services.memory.hybrid_search import hybrid_search


def search(user_message, limit=5):

    return hybrid_search(
        user_message,
        limit,
    )