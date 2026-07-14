
import { useEffect, useState } from "react";

import ChatHeader from "../components/chat/ChatHeader";
import ChatMessages from "../components/chat/ChatMessages";
import ChatInput from "../components/chat/ChatInput";
import { sendMessage, resetChat  } from "../services/chatService";


interface Message {
  id: number;
  sender: "user" | "ai";
  message: string;
  time: string;
}

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>(() => {
    const savedMessages = localStorage.getItem("messages");

    if (savedMessages) {
      return JSON.parse(savedMessages) as Message[];
    }

    return [
      {
        id: 1,
        sender: "ai",
        message: "Hello Neil! 👋 How are you feeling today?",
        time: "10:32 AM",
      }
    ];
  });

  const [isTyping, setIsTyping] = useState(false);
  const [isLoading, setIsLoading] = useState(false);



  useEffect(() => {
    localStorage.setItem("messages", JSON.stringify(messages));
  }, [messages]);

  async function handleSend(message: string) {
    try {
      const newMessage: Message = {
        id: Date.now(),
        sender: "user",
        message,
        time: new Date().toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        }),
      };

      setMessages((prev) => [...prev, newMessage]);

      setIsLoading(true);
      setIsTyping(true);

      const reply = await sendMessage(message);

      const aiReply: Message = {
        id: Date.now() + 1,
        sender: "ai",
        message: reply,
        time: new Date().toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        }),
      };

      setTimeout(() => {
        setMessages((prev) => [...prev, aiReply]);
        setIsTyping(false);
        setIsLoading(false);
      }, 1000);
    } catch (error) {
      console.error("Failed to send message:", error);

      setIsTyping(false);
      setIsLoading(false);
    }
  }

  async function handleClearChat() {
    try {
      await resetChat();

      localStorage.removeItem("messages");

      setMessages([
        {
          id: 1,
          sender: "ai",
          message: "Hello Neil! 👋 How are you feeling today?",
          time: new Date().toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          }),
        },
      ]);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div
      className="container-fluid d-flex flex-column"
      style={{ height: "100vh" }}
    >
      <ChatHeader />

      <div className="p-2 border-bottom">
        <button
          className="btn btn-outline-danger btn-sm"
          onClick={handleClearChat}
        >
          🗑 Clear Chat
        </button>
      </div>

      <div className="flex-grow-1 overflow-auto" style={{ minHeight: 0 }}>
        <ChatMessages messages={messages} isTyping={isTyping} />
      </div>

      <ChatInput onSend={handleSend} isLoading={isLoading} />
    </div>
  );
}

