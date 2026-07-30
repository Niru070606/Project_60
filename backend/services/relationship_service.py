from repositories.relationship_repository import (
    get_relationship,
    update_relationship,
)


def reinforce_relationship():

    relationship = get_relationship()

    update_relationship(
        relationship,
        familiarity=1,
    )

def apply_relationship_changes(changes):

    relationship = get_relationship()

    update_relationship(
        relationship,
        trust=changes.get("trust", 0),
        familiarity=changes.get("familiarity", 0),
        comfort=changes.get("comfort", 0),
        humor=changes.get("humor", 0),
        emotional_closeness=changes.get(
            "emotional_closeness",
            0,
        ),
    )