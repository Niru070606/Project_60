import { Brain, MessageCircle, Smile, Users } from "lucide-react";

import StatCard from "./StatCard";

export default function StatsGrid() {
  return (
    <div className="row g-4 mb-4">
      <div className="col-lg-3 col-md-6">
        <StatCard title="Memories" value={124} icon={<Brain size={28} />} />
      </div>

      <div className="col-lg-3 col-md-6">
        <StatCard title="Chats" value={58} icon={<MessageCircle size={28} />} />
      </div>

      <div className="col-lg-3 col-md-6">
        <StatCard title="Mood" value="Happy" icon={<Smile size={28} />} />
      </div>

      <div className="col-lg-3 col-md-6">
        <StatCard
          title="Personality"
          value="Curious"
          icon={<Users size={28} />}
        />
      </div>
    </div>
  );
}
