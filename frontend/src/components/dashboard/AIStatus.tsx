import "../../styles/dashboard/ai-status.css";

import { useEffect, useState } from "react";

import { getMemories, getMessages, getPersonality } from "../../services/DashboardApi";

interface StatusItem {
  label: string;
  value: string | number;
}

export default function AIStatus() {
  const [statusItems, setStatusItems] = useState<StatusItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadStatus() {
      try {
        const [memories, messages, personality] = await Promise.allSettled([
          getMemories(),
          getMessages(),
          getPersonality(),
        ]);

        const items: StatusItem[] = [];

        items.push({
          label: "Memories",
          value: memories.status === "fulfilled" ? `${memories.value.length} Memories` : "0 Memories",
        });

        const lastMessage =
          messages.status === "fulfilled" && messages.value.length > 0
            ? messages.value[messages.value.length - 1]
            : null;

        items.push({
          label: "Last Conversation",
          value: lastMessage ? lastMessage.time : "None yet",
        });

        const personalityName =
          personality.status === "fulfilled" && personality.value?.identity?.name
            ? personality.value.identity.name
            : "Project-60";

        items.push({
          label: "Model",
          value: personalityName,
        });

        items.push({
          label: "Status",
          value: "🟢 Online",
        });

        items.push({
          label: "Growth Stage",
          value: "Baby",
        });

        items.push({
          label: "System Health",
          value: "Excellent",
        });

        setStatusItems(items);
      } catch {
        setStatusItems([
          { label: "Status", value: "🟡 Connecting..." },
          { label: "Model", value: "Project-60" },
          { label: "Growth Stage", value: "Baby" },
          { label: "Memories", value: "0 Memories" },
          { label: "System Health", value: "Unknown" },
          { label: "Last Conversation", value: "None yet" },
        ]);
      } finally {
        setLoading(false);
      }
    }

    loadStatus();
  }, []);

  return (
    <div className="card-theme ai-status">
      <h4 className="section-title">AI Status</h4>

      <div className="status-grid">
        {statusItems.map((item, index) => (
          <div className="status-item" key={index}>
            <span>{item.label}</span>
            <strong>{loading ? "..." : item.value}</strong>
          </div>
        ))}
      </div>
    </div>
  );
}