from database import db


class Relationship(db.Model):
    __tablename__ = "relationships"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    conversation_id = db.Column(
        db.Integer,
        db.ForeignKey("conversations.id"),
        nullable=False,
        unique=True,
    )

    trust = db.Column(
        db.Integer,
        default=50,
    )

    familiarity = db.Column(
        db.Integer,
        default=50,
    )

    comfort = db.Column(
        db.Integer,
        default=50,
    )

    humor = db.Column(
        db.Integer,
        default=50,
    )

    respect = db.Column(
        db.Integer,
        default=100,
    )

    emotional_closeness = db.Column(
        db.Integer,
        default=50,
    )