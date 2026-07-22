from services.memory_service import load_memories


def search_memories(user_message: str):

    memories = load_memories()

    if not memories:
        return []

    user_message = user_message.lower()

    relevant = []

    for memory in memories:

        if any(
            word in memory.memory.lower()
            for word in user_message.split()
        ):
            relevant.append(memory)

    return relevant