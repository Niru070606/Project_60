from services.memory.semantic_search import (
    find_semantically_similar_memory,
)


def consolidate_memory(
    reflection,
    conversation_id,
):
    similar_memories = find_semantically_similar_memory(
        reflection["memory"],
        limit=1,
        threshold=0.85,
    )

    if not similar_memories:

        return {
            "action": "new",
            "memory": reflection,
        }

    existing, score = similar_memories[0]

    if score >= 0.90:

        return {
            "action": "skip",
            "memory": existing,
            "score": score,
        }

    return {
        "action": "update",
        "memory": existing,
        "score": score,
    }