
import { useEffect, useState } from "react";

import ChatHeader from "../components/chat/ChatHeader";
import ChatMessages from "../components/chat/ChatMessages";
import ChatInput from "../components/chat/ChatInput";
import { sendMessage, resetChat  } from "../services/chatService";
import { getMessages } from "../services/messageService";


interface Message {
  id: number;
  sender: "user" | "ai";
  message: string;
  time: string;
}

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);

  const [isTyping, setIsTyping] = useState(false);
  const [isLoading, setIsLoading] = useState(false);



  async function loadMessages() {
    try {
      const data = await getMessages();

      if (data.length === 0) {
        setMessages([
          {
            id: 1,
            sender: "ai",
            message: "Hello Neil! 👋 How are you feeling today?",
            time: "10:32 AM",
          },
        ]);
      } else {
        setMessages(data);
      }
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    loadMessages();
  }, []);

  async function handleSend(message: string) {
    try {
      setIsLoading(true);
      setIsTyping(true);

      await sendMessage(message);

      await loadMessages();

      setIsTyping(false);
      setIsLoading(false);;
    } catch (error) {
      console.error("Failed to send message:", error);

      setIsTyping(false);
      setIsLoading(false);
    }
  }

  async function handleClearChat() {
    try {
      await resetChat();
      setMessages([]);
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

