import "./../../styles/dashboard/quick-actions.css";

import { MessageCircle, Brain, BarChart3, Settings } from "lucide-react";

export default function QuickActions() {
  const actions = [
    {
      title: "Start Chat",
      icon: <MessageCircle size={20} />,
    },
    {
      title: "Memories",
      icon: <Brain size={20} />,
    },
    {
      title: "Analytics",
      icon: <BarChart3 size={20} />,
    },
    {
      title: "Settings",
      icon: <Settings size={20} />,
    },
  ];

  return (
    <div className="card-theme quick-actions">
      <h4 className="section-title">Quick Actions</h4>

      <div className="action-grid">
        {actions.map((action, index) => (
          <button key={index} className="action-btn">
            {action.icon}
            <span>{action.title}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
