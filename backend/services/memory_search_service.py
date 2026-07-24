import re

from services.memory_service import load_memories
from repositories.memory_repository import increment_retrieval_count


STOP_WORDS = {
    "i",
    "am",
    "is",
    "are",
    "the",
    "a",
    "an",
    "of",
    "to",
    "for",
    "and",
    "my",
    "me",
    "you",
    "your",
    "in",
    "on",
    "at",
}


def normalize(text: str) -> str:
    """Lowercase and remove punctuation."""

    text = text.lower()

    text = re.sub(r"[^a-z0-9\s]", "", text)

    return text


def search_memories(user_message: str, limit: int = 5):
    """
    Search the most relevant memories using keyword matching.
    Returns only the highest-ranked memories.
    """

    memories = load_memories()

    if not memories:
        return []

    words = {
        word
        for word in normalize(user_message).split()
        if word not in STOP_WORDS
    }

    scored = []

    for memory in memories:

        memory_words = {
            word
            for word in normalize(memory.memory).split()
            if word not in STOP_WORDS
        }

        matches = len(words & memory_words)

        if matches == 0:
            continue

        score = (
            matches * 10
        ) + memory.importance

        scored.append(
            (score, memory)
        )

    scored.sort(
        key=lambda x: x[0],
        reverse=True,
    )

    top_memories = [
    memory
    for _, memory in scored[:limit]
    ]

    for memory in top_memories:
        increment_retrieval_count(memory)

    return top_memories