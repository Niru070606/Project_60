export async function getMessages() {
  const response = await fetch("http://127.0.0.1:5000/messages");

  if (!response.ok) {
    throw new Error("Failed to load messages.");
  }

  return await response.json();
}
