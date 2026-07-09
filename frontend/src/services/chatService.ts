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

  console.log(response);
  const data = await response.json();
  console.log(data);

  return data.reply;
}
