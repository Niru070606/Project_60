from services.history_service import get_recent_messages


def build_history(limit: int = 10):

    messages = get_recent_messages(limit=limit)

    history = []

    for msg in messages:
        history.append(
            f"{msg.sender}: {msg.message}"
        )

    return "\n".join(history)