from database import db
from models.conversation import Conversation


def get_or_create_conversation():
    conversation = Conversation.query.first()

    if conversation is None:
        conversation = Conversation()

        db.session.add(conversation)
        db.session.commit()

    return conversation


def get_conversation(conversation_id: int):
    return db.session.get(Conversation, conversation_id)


def delete_conversation(conversation: Conversation):
    db.session.delete(conversation)
    db.session.commit()