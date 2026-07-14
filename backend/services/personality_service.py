current_personality = {}

print("personality_service loaded:", id(current_personality))


def save_personality(personality: dict):
    global current_personality
    current_personality = personality
    print("Saved id:", id(current_personality))


def get_personality():
    print("Read id:", id(current_personality))
    return current_personality