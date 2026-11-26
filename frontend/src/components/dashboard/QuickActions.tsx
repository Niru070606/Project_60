import "../../styles/dashboard/quick-actions.css";

import { useNavigate } from "react-router-dom";
import { MessageCircle, Brain, BarChart3, Settings } from "lucide-react";

export default function QuickActions() {
  const navigate = useNavigate();

  const actions = [
    {
      title: "Start Chat",
      icon: <MessageCircle size={20} />,
      onClick: () => navigate("/chat"),
    },
    {
      title: "Memories",
      icon: <Brain size={20} />,
      onClick: () => navigate("/memories"),
    },
    {
      title: "Analytics",
      icon: <BarChart3 size={20} />,
      onClick: () => navigate("/analytics"),
    },
    {
      title: "Settings",
      icon: <Settings size={20} />,
      onClick: () => navigate("/settings"),
    },
  ];

  return (
    <div className="card-theme quick-actions">
      <h4 className="section-title">Quick Actions</h4>

      <div className="action-grid">
        {actions.map((action, index) => (
          <button key={index} className="action-btn" onClick={action.onClick}>
            {action.icon}
            <span>{action.title}</span>
          </button>
        ))}
      </div>
    </div>
  );
}