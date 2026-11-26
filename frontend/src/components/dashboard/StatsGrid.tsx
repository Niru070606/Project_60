import "../../styles/dashboard/stat-card.css";

import { useEffect, useState } from "react";
import { Brain, MessageCircle, Smile, Users } from "lucide-react";

import StatCard from "./StatCard";

import { getMemories, getMessages, getPersonality } from "../../services/DashboardApi";

export default function StatsGrid() {
  const [stats, setStats] = useState({
    memoryCount: 0,
    chatCount: 0,
    mood: "Happy",
    personalityTrait: "Curious",
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadStats() {
      try {
        const [memories, messages, personality] = await Promise.allSettled([
          getMemories(),
          getMessages(),
          getPersonality(),
        ]);

        const moodValues = ["Happy", "Excited", "Curious", "Peaceful", "Focused", "Joyful"];
        const moodIndex = Math.floor(Math.random() * moodValues.length);

        setStats({
          memoryCount: memories.status === "fulfilled" ? memories.value.length : 0,
          chatCount: messages.status === "fulfilled" ? messages.value.length : 0,
          mood: moodValues[moodIndex],
          personalityTrait:
            personality.status === "fulfilled" && personality.value?.relationship?.relationshipType
              ? personality.value.relationship.relationshipType
              : "Curious",
        });
      } catch {
        setStats({
          memoryCount: 0,
          chatCount: 0,
          mood: "Unknown",
          personalityTrait: "Unknown",
        });
      } finally {
        setLoading(false);
      }
    }

    loadStats();
  }, []);

  return (
    <div className="row g-4 mb-4">
      <div className="col-lg-3 col-md-6">
        <StatCard
          className={loading ? "loading" : ""}
          title="Memories"
          value={loading ? "..." : stats.memoryCount}
          icon={<Brain size={28} />}
        />
      </div>

      <div className="col-lg-3 col-md-6">
        <StatCard
          className={loading ? "loading" : ""}
          title="Chats"
          value={loading ? "..." : stats.chatCount}
          icon={<MessageCircle size={28} />}
        />
      </div>

      <div className="col-lg-3 col-md-6">
        <StatCard
          className={loading ? "loading" : ""}
          title="Mood"
          value={loading ? "..." : stats.mood}
          icon={<Smile size={28} />}
        />
      </div>

      <div className="col-lg-3 col-md-6">
        <StatCard
          className={loading ? "loading" : ""}
          title="Personality"
          value={loading ? "..." : stats.personalityTrait}
          icon={<Users size={28} />}
        />
      </div>
    </div>
  );
}