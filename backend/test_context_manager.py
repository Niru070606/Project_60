from services.brain.context_manager import should_load_memory


intent = "chat"

result = should_load_memory(intent)

print("\n===== MEMORY LOAD TEST =====")
print("Intent:", intent)
print("Should load memory:", result)
print("============================")