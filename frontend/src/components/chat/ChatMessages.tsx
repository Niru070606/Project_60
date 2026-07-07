import "./../../styles/chat/chat-messages.css";
import { useEffect, useRef } from "react";

import MessageBubble from "./MessageBubble";

interface Message {
  id: number;
  sender: "user" | "ai";
  message: string;
  time: string;
}

interface ChatMessagesProps {
  messages: Message[];
  isTyping: boolean;
}

export default function ChatMessages({
  messages,
  isTyping,
}: ChatMessagesProps) {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);
  return (
    <div className="chat-messages">
      {messages.map((msg) => (
        <MessageBubble
          key={msg.id}
          sender={msg.sender}
          message={msg.message}
          time={msg.time}
        />
      ))}

      {isTyping && (
        <div className="typing-indicator">Project-60 is typing...</div>
      )}
      <div ref={bottomRef}></div>
    </div>
  );
}
