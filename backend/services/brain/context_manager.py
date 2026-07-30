def should_load_identity(intent: str) -> bool:
    return True


def should_load_memory(intent: str) -> bool:
    return intent in {
        "memory",
        "relationship",
        "programming",
    }


def should_load_relationship(intent: str) -> bool:
    return intent in {
        "relationship",
        "chat",
        "memory",
    }


def should_load_history(intent: str) -> bool:
    return True


def should_load_rules(intent: str) -> bool:
    return True