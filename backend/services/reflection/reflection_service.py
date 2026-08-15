from repositories.conversation_repository import (
    get_or_create_conversation,
)

from repositories.memory_repository import (
    get_unreflected_memories,
    mark_reflected,
    update_memory,
)

from services.memory_service import (
    save_extracted_memories,
)

from services.reflection.reflection_engine import (
    reflect,
)

from services.reflection.reflection_validator import (
    validate_reflections,
)

from services.reflection.memory_consolidator import (
    consolidate_memory,
)

from services.memory.embedding_sync import (
    sync_memory_embedding,
)

def run_reflection():
    conversation = get_or_create_conversation()
    memories = get_unreflected_memories()

    if not memories:
        return []

    reflections = reflect(
        memories
    )

    reflections = validate_reflections(
        reflections,
        conversation.id,
    )

    if not reflections:
        mark_reflected(memories)
        return []

    for reflection in reflections:

        result = consolidate_memory(
            reflection,
            conversation.id,
        )

        if result["action"] == "new":

            new_memories = save_extracted_memories([
                reflection
            ])

            for memory in new_memories:

                sync_memory_embedding(
                    memory
                )

        elif result["action"] == "update":

            existing = result["memory"]

            update_memory(
                existing,
                reflection["memory"],
                reflection["importance"],
            )

            sync_memory_embedding(
                existing
            )
            
    mark_reflected(
        memories
    )

    return reflections