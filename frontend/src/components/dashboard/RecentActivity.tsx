import "../../styles/dashboard/recent-activity.css";

import { useEffect, useState } from "react";
import { Brain, MessageCircle, Smile } from "lucide-react";

import { getMemories, getMessages } from "../../services/DashboardApi";

interface Activity {
  title: string;
  time: string;
  icon: React.ReactNode;
}

export default function RecentActivity() {
  const [activities, setActivities] = useState<Activity[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadActivities() {
      try {
        const [memories, messages] = await Promise.all([
          getMemories(),
          getMessages(),
        ]);

        const newActivities: Activity[] = [];

        if (memories && memories.length > 0) {
          const latestMemory = memories[0];
          newActivities.push({
            title: `New memory saved: "${latestMemory.memory.substring(0, 50)}..."`,
            time: latestMemory.created_at || "Recently",
            icon: <Brain size={18} />,
          });
        }

        if (messages && messages.length > 0) {
          const latestMessages = messages.slice(-3).reverse();
          latestMessages.forEach((msg) => {
            newActivities.unshift({
              title: `${msg.sender === "ai" ? "AI" : "You"}: ${msg.message.substring(0, 40)}${msg.message.length > 40 ? "..." : ""}`,
              time: msg.time || "Just now",
              icon: <MessageCircle size={18} />,
            });
          });
        }

        if (newActivities.length === 0) {
          newActivities.push({
            title: "No recent activity yet",
            time: "---",
            icon: <Smile size={18} />,
          });
        }

        setActivities(newActivities.slice(0, 6));
      } catch (error) {
        setActivities([
          {
            title: "No recent activity yet",
            time: "---",
            icon: <Smile size={18} />,
          },
        ]);
      } finally {
        setLoading(false);
      }
    }

    loadActivities();
  }, []);

  return (
    <div className="card-theme recent-activity">
      <h4 className="section-title">Recent Activity</h4>

      {activities.map((activity, index) => (
        <div key={index} className="activity-item">
          <div className="activity-icon">{activity.icon}</div>

          <div className="activity-content">
            <h6>{loading ? "..." : activity.title}</h6>
            <span>{activity.time}</span>
          </div>
        </div>
      ))}
    </div>
  );
}