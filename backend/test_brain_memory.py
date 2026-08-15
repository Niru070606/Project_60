from app import app

from services.brain.memory import build_memory


with app.app_context():

    query = "What school am I studying at?"

    result = build_memory(query)

    print("\n===== BRAIN MEMORY TEST =====")
    print(result)
    print("=============================")