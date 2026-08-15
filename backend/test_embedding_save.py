from app import app
from repositories.memory_embedding_repository import save_embedding

with app.app_context():

    result = save_embedding(
        memory_id=87,
        model="test-model",
        embedding="[0.1, 0.2, 0.3]"
    )

    print("Saved embedding ID:", result.id)