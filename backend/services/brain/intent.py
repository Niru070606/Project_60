PROGRAMMING = {
    "python",
    "flask",
    "react",
    "javascript",
    "java",
    "sql",
    "database",
    "html",
    "css",
    "bootstrap",
    "bug",
    "error",
    "code",
    "coding",
    "programming",
}

MEMORY = {
    "remember",
    "memory",
    "know",
    "who",
    "about",
}

RELATIONSHIP = {
    "love",
    "friend",
    "relationship",
    "trust",
    "feel",
    "emotion",
    "miss",
}

LEARNING = {
    "teach",
    "explain",
    "how",
    "why",
    "difference",
    "meaning",
}


def detect_intent(message: str) -> str:

    text = message.lower()

    words = set(text.split())

    if words & MEMORY:
        return "memory"

    if words & PROGRAMMING:
        return "programming"

    if words & RELATIONSHIP:
        return "relationship"

    if words & LEARNING:
        return "learning"

    return "chat"