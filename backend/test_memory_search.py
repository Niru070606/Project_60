from app import app

from services.memory.embedding_service import create_embedding
from services.memory.vector_index import get_candidate_embeddings
from services.memory.similarity import cosine_similarity

import json


with app.app_context():

    query = "What school am I studying at?"

    user_embedding = create_embedding(query)

    embeddings = get_candidate_embeddings()

    SIMILARITY_THRESHOLD = 0.60

    results = []

    for embedding in embeddings:

        stored_embedding = json.loads(
            embedding.embedding
        )

        score = cosine_similarity(
            user_embedding,
            stored_embedding,
        )

        results.append(
            (
                embedding.memory_id,
                score,
            )
        )

    results.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    print("\n===== SEMANTIC SEARCH TEST =====")
    print("Query:", query)
    print("Threshold:", SIMILARITY_THRESHOLD)
    print()

    for memory_id, score in results[:10]:

        status = (
            "✅ PASS"
            if score >= SIMILARITY_THRESHOLD
            else "❌ REJECT"
        )

        print(
            f"Memory ID: {memory_id} | "
            f"Score: {score:.6f} | "
            f"{status}"
        )

    print("\n===== MEMORY 22 =====")

    memory_22 = next(
        (
            (memory_id, score)
            for memory_id, score in results
            if memory_id == 22
        ),
        None,
    )

    if memory_22:

        memory_id, score = memory_22

        print("Memory ID:", memory_id)
        print(f"Score: {score:.6f}")

        if score >= SIMILARITY_THRESHOLD:
            print("🔥 Memory 22 PASSES the threshold!")
        else:
            print("❌ Memory 22 is below the threshold.")

    else:
        print("Memory 22 was not found.")

    print("===============================")