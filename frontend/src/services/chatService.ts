export async function sendMessage(message: string) {
  const response = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
    }),
  });

  if (!response.ok) {
    const text = await response.text().catch(() => "");
    throw new Error(`Backend error ${response.status}: ${text}`);
  }

  const data = await response.json();
  return data.reply;
}

export async function resetChat() {
  await fetch("http://127.0.0.1:5000/chat/reset", {
    method: "POST",
  });
}
