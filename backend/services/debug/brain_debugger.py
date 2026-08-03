from pprint import pprint


def debug_brain(brain):

    print("\n========== PROJECT-60 BRAIN ==========\n")

    print("Intent")
    print("--------------------------------------")
    print(brain.intent)

    print("\nThought")
    print("--------------------------------------")
    pprint(brain.thought)

    print("\nLoaded Modules")
    print("--------------------------------------")
    print("Identity     :", bool(brain.identity))
    print("Relationship :", bool(brain.relationship))
    print("Memory       :", bool(brain.memory))
    print("History      :", bool(brain.history))
    print("Rules        :", bool(brain.rules))

    print("\nThought Prompt")
    print("--------------------------------------")
    print(brain.thought_prompt)

    print("\n======================================\n")

    print("\n========== BEHAVIOR ==========")
    print(brain.behavior)
    print("==============================\n")

    print("\nBehavior Prompt")
    print("--------------------------------------")
    print(brain.behavior_prompt)


