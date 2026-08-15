from app import app

from services.brain.builder import build_brain


with app.app_context():

    query = "What school am I studying at?"

    brain = build_brain(query)

    print("\n===== BRAIN TEST =====")

    print("\n--- INTENT ---")
    print(brain.intent)

    print("\n--- MEMORY ---")
    print(brain.memory)

    print("\n--- SYSTEM PROMPT ---")
    print(brain.system_prompt)

    print("======================")