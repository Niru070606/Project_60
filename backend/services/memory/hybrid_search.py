from services.memory.keyword_search import (
    search_memories,
)

from services.memory.semantic_search import (
    semantic_search,
)


def hybrid_search(
    user_message: str,
    limit: int = 5,
):

    keyword_results = search_memories(
        user_message,
        limit=limit,
    ) or []

    semantic_results = semantic_search(
        user_message,
        limit=limit,
    ) or []

    combined = {}

    # Keyword search returns Memory objects.
    for memory in keyword_results:

        keyword_score = memory.importance

        combined[memory.id] = {
            "memory": memory,
            "keyword_score": keyword_score,
            "semantic_score": 0.0,
        }

    # Semantic search returns (Memory, similarity_score).
    for memory, score in semantic_results:

        if memory.id not in combined:

            combined[memory.id] = {
                "memory": memory,
                "keyword_score": 0,
                "semantic_score": score,
            }

        else:

            combined[memory.id][
                "semantic_score"
            ] = score

    ranked = []

    for item in combined.values():

        memory = item["memory"]

        keyword_score = item["keyword_score"]

        semantic_score = item["semantic_score"]

        importance_score = (
            memory.importance / 100
        )

        retrieval_score = min(
            memory.retrieval_count / 100,
            1.0,
        )

        final_score = (
            (semantic_score * 0.40)
            +
            ((keyword_score / 100) * 0.30)
            +
            (importance_score * 0.20)
            +
            (retrieval_score * 0.10)
        )

        ranked.append(
            (
                memory,
                final_score,
            )
        )

    ranked.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    return [
        memory
        for memory, _ in ranked[:limit]
    ]