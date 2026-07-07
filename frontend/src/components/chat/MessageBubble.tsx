import "./../../styles/chat/message-bubble.css";

interface MessageBubbleProps {
  sender: "user" | "ai";
  message: string;
  time: string;
}

export default function MessageBubble({
  sender,
  message,
  time,
}: MessageBubbleProps) {
  return (
    <div className={sender === "user" ? "message-row user" : "message-row ai"}>
      <div className="message-bubble">
        <p>{message}</p>

        <span>{time}</span>
      </div>
    </div>
  );
}
