"""
Periodic Memory Merge Task

Run this periodically (e.g., daily via cron) to consolidate similar memories
across the entire database. Reduces storage and token usage by merging
overlapping memories.
"""

from app import app
from services.memory.memory_merger import run_memory_merge
from repositories.conversation_repository import get_or_create_conversation


def run_periodic_memory_merge(similarity_threshold=0.75):
    """
    Run memory consolidation for the current conversation.
    Can be called from a scheduled task/cron job.

    Args:
        similarity_threshold: Minimum text similarity to consider merging (0.0-1.0)

    Returns:
        dict with merge statistics
    """
    with app.app_context():
        conversation = get_or_create_conversation()

        merges_done = run_memory_merge(
            conversation.id,
            similarity_threshold=similarity_threshold
        )

        return {
            "conversation_id": conversation.id,
            "merges_performed": merges_done,
            "threshold_used": similarity_threshold,
        }


if __name__ == "__main__":
    result = run_periodic_memory_merge()
    print(f"Memory merge complete: {result}")