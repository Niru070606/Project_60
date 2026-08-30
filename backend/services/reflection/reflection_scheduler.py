from services.reflection.reflection_service import (
    run_reflection,
)

REFLECTION_INTERVAL = 5


def should_reflect(
    message_count: int,
):

    return (
        message_count > 0
        and
        message_count % REFLECTION_INTERVAL == 0
    )


def process_reflection(
    message_count: int,
):

    if should_reflect(
        message_count
    ):

        print(
            "\n🧠 Running Reflection...\n"
        )

        return run_reflection()

    return []