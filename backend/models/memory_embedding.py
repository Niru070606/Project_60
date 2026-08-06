from database import db


class MemoryEmbedding(db.Model):
    __tablename__ = "memory_embeddings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    memory_id = db.Column(
        db.Integer,
        db.ForeignKey("memories.id"),
        nullable=False,
        unique=True
    )

    model = db.Column(
        db.String(100),
        nullable=False
    )

    embedding = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )
    