from repositories.conversation_repository import get_or_create_conversation
from models.relationship import Relationship
from database import db


def get_relationship():

    conversation = get_or_create_conversation()

    relationship = (
        Relationship.query
        .filter_by(
            conversation_id=conversation.id
        )
        .first()
    )

    if relationship is None:

        relationship = Relationship(
            conversation_id=conversation.id
        )

        db.session.add(relationship)
        db.session.commit()

    return relationship


def update_relationship(
    relationship,
    trust=0,
    familiarity=0,
    comfort=0,
    humor=0,
    emotional_closeness=0,
):

    relationship.trust = max(
        0,
        min(100, relationship.trust + trust)
    )

    relationship.familiarity = max(
        0,
        min(100, relationship.familiarity + familiarity)
    )

    relationship.comfort = max(
        0,
        min(100, relationship.comfort + comfort)
    )

    relationship.humor = max(
        0,
        min(100, relationship.humor + humor)
    )

    relationship.emotional_closeness = max(
        0,
        min(100, relationship.emotional_closeness + emotional_closeness)
    )

    db.session.commit()

    return relationship