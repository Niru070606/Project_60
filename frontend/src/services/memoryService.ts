const API_URL = "http://127.0.0.1:5000";

export async function getMemories() {
  const response = await fetch(`${API_URL}/memories`);

  if (!response.ok) {
    throw new Error("Failed to fetch memories");
  }

  return response.json();
}

export async function deleteMemory(id: number) {
  const response = await fetch(`${API_URL}/memories/${id}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Failed to delete memory");
  }

  return response.json();
}
