from services.memory_service import load_memories

SYNONYMS = {
    "frontend": [
        "react",
        "html",
        "css",
        "javascript",
        "bootstrap",
    ],
    "backend": [
        "flask",
        "python",
        "api",
        "database",
    ],
    "college": [
        "bsit",
        "school",
        "university",
        "pup",
    ],
    "coding": [
        "programming",
        "python",
        "react",
        "flask",
        "javascript",
    ],
}


def retrieve_memories(user_message: str):

    memories = load_memories()

    if not memories:
        return []

    query = user_message.lower()

    search_words = set(query.split())

    for word in list(search_words):
        if word in SYNONYMS:
            search_words.update(SYNONYMS[word])

    results = []

    for memory in memories:

        score = memory.importance

        # Exact sentence match
        if query in memory.memory.lower():
            score += 30

            results.append((score, memory))
            continue

        # Keyword / synonym matches
        for word in search_words:
            if word in memory.memory.lower():
                score += 5

        if score > memory.importance:
            results.append((score, memory))

    results.sort(
        key=lambda item: item[0],
        reverse=True,
    )

    return [
        memory
        for score, memory in results[:10]
    ]