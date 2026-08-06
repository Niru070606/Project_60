import os

from google import genai

from config import Config


client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)

import json

from repositories.memory_embedding_repository import (
    save_embedding,
)


MODEL = "gemini-embedding-001"


def create_embedding(text: str):

    response = client.models.embed_content(
        model=MODEL,
        contents=text
    )

    return response.embeddings[0].values

def create_and_store_embedding(
    memory_id: int,
    text: str,
):
    embedding = create_embedding(text)

    embedding_json = json.dumps(
        embedding
    )

    save_embedding(
        memory_id=memory_id,
        model=MODEL,
        embedding=embedding_json,
    )