import "./../../styles/dashboard/recent-activity.css";

import { Brain, MessageCircle, Smile } from "lucide-react";

const activities = [
  {
    title: "New memory saved",
    time: "2 hours ago",
    icon: <Brain size={18} />,
  },
  {
    title: "Conversation completed",
    time: "Yesterday",
    icon: <MessageCircle size={18} />,
  },
  {
    title: "Mood updated",
    time: "2 days ago",
    icon: <Smile size={18} />,
  },
];

export default function RecentActivity() {
  return (
    <div className="card-theme recent-activity">
      <h4 className="section-title">Recent Activity</h4>

      {activities.map((activity, index) => (
        <div key={index} className="activity-item">
          <div className="activity-icon">{activity.icon}</div>

          <div className="activity-content">
            <h6>{activity.title}</h6>
            <span>{activity.time}</span>
          </div>
        </div>
      ))}
    </div>
  );
}
