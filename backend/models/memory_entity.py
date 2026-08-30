from database import db


class MemoryEntity(db.Model):

    __tablename__ = "memory_entities"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    memory_id = db.Column(
        db.Integer,
        db.ForeignKey("memories.id"),
        nullable=False
    )

    entity_id = db.Column(
        db.Integer,
        db.ForeignKey("entities.id"),
        nullable=False
    )

    memory = db.relationship(
        "Memory",
        backref="memory_entities",
    )

    entity = db.relationship(
        "Entity",
        backref="memory_entities",
    )

    __table_args__ = (
        db.UniqueConstraint(
            "memory_id",
            "entity_id",
            name="uq_memory_entity",
        ),
    )