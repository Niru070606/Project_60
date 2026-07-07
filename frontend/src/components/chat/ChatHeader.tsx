import "./../../styles/chat/chat-header.css";

import { Bot } from "lucide-react";

export default function ChatHeader() {
  return (
    <header className="card-theme chat-header">
      <div className="chat-info">
        <div className="chat-avatar">
          <Bot size={28} />
        </div>

        <div>
          <h4>Project-60</h4>
          <span>🟢 Online</span>
        </div>
      </div>
    </header>
  );
}
