from services.memory.hybrid_search import (
    hybrid_search,
)


WORKING_MEMORY_LIMIT = 5


def build_working_memory(
    user_message: str,
):

    memories = hybrid_search(
        user_message,
        limit=WORKING_MEMORY_LIMIT,
    )

    return memories