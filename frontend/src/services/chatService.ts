const aiReplies = [
  "Hello Neil! 👋",
  "That's interesting.",
  "Tell me more.",
  "I'm listening.",
  "How does that make you feel?",
  "I understand.",
  "Interesting thought!",
  "Can you explain that further?",
  "Let's think about that together.",
  "That sounds exciting!",
];

export async function sendMessage(message: string) {
  const randomReply = aiReplies[Math.floor(Math.random() * aiReplies.length)];

  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(randomReply);
    }, 1000);

});
}
