
def get_memory_limit(intent: str) -> int:

    limits = {
        "memory": 10,
        "relationship": 6,
        "programming": 4,
        "learning": 3,
        "chat": 2,
    }

    return limits.get(intent, 3)


def get_history_limit(intent: str) -> int:

    limits = {
        "memory": 12,
        "relationship": 10,
        "programming": 8,
        "learning": 6,
        "chat": 5,
    }

    return limits.get(intent, 5)