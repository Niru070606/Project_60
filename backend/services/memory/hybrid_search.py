from services.memory.keyword_search import (
    search_memories,
)

from services.memory.semantic_search import (
    semantic_search,
)

from services.memory_entity_service import (
    get_memories_for_entities,
)

from services.memory.entity_candidates import (
    extract_entity_candidates,
)

from services.memory.entity_interpreter import (
    interpret_entities,
)

from services.memory.entity_candidate_merger import (
    merge_entity_candidates,
)

from services.memory.entity_resolver import (
    resolve_entities,
)

def hybrid_search(
    user_message: str,
    limit: int = 5,
):
    entity_candidates = extract_entity_candidates(
        user_message
    )

    interpreted_entities = interpret_entities(
        user_message,
        entity_candidates
    )

    merged_entities = merge_entity_candidates(
        interpreted_entities
    )

    resolved_entities = resolve_entities(
        merged_entities
    )

    entity_ids = [
        entity.id
        for entity in resolved_entities
    ]

    entity_memories = get_memories_for_entities(
        entity_ids
    )

    # print("\n===== ENTITY RETRIEVAL TEST =====")

    # print(
    #     "Resolved entity IDs:",
    #     entity_ids,
    # )

    # for memory in entity_memories:
    #     print(
    #         "Entity memory:",
    #         memory.id,
    #         "|",
    #         memory.memory,
    #     )

    # print("===============================")

    keyword_results = search_memories(
        user_message,
        limit=limit,
    ) or []

    # print("\n===== KEYWORD RESULT TEST =====")
    # print(keyword_results)

    # for result in keyword_results:
    #     print("TYPE:", type(result))
    #     print("VALUE:", result)

    # print("==============================")

    semantic_results = semantic_search(
        user_message,
        limit=limit,
    ) or []

    combined = {}

    # Keyword search returns Memory objects.
    for memory, score in keyword_results:

        keyword_score = score

        combined[memory.id] = {
            "memory": memory,
            "keyword_score": keyword_score,
            "semantic_score": 0.0,
            "entity_match": False,
        }

    # Semantic search returns (Memory, similarity_score).
    for memory, score in semantic_results:

        if memory.id not in combined:

            combined[memory.id] = {
                "memory": memory,
                "keyword_score": 0.0,
                "semantic_score": score,
                "entity_match": False,
            }

        else:

            combined[memory.id][
                "semantic_score"
            ] = score

        # --------------------------------
    # Add entity-based memories
    # --------------------------------

    for memory in entity_memories:

        if memory.id not in combined:

            combined[memory.id] = {
                "memory": memory,
                "keyword_score": 0.0,
                "semantic_score": 0.0,
                "entity_match": True,
            }

        else:

            combined[memory.id][
                "entity_match"
            ] = True

    ranked = []

    for item in combined.values():

        memory = item["memory"]

        keyword_score = item["keyword_score"]

        semantic_score = item["semantic_score"]

        entity_score = 1.0 if item["entity_match"] else 0.0

        importance_score = (
            memory.importance / 100
        )

        retrieval_score = min(
            memory.retrieval_count / 100,
            1.0,
        )

        final_score = (
            (semantic_score * 0.35)
            +
            ((keyword_score / 100) * 0.25)
            +
            (importance_score * 0.20)
            +
            (retrieval_score * 0.10)
            +
            (entity_score * 0.10)
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

    # print("\n===== HYBRID SEARCH RESULTS =====")

    # for memory, score in ranked[:limit]:
    #     print(
    #         f"Memory ID: {memory.id} | "
    #         f"Score: {score:.6f} | "
    #         f"Memory: {memory.memory}"
    #     )

    # print("==============================")

    return [
        memory
        for memory, _ in ranked[:limit]
    ]