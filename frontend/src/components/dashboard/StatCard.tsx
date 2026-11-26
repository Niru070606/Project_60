import "../../styles/dashboard/stat-card.css";

import type { ReactNode } from "react";

interface StatCardProps {
  title: string;
  value: string | number;
  icon: ReactNode;
  className?: string;
}

export default function StatCard({
  title,
  value,
  icon,
  className = "",
}: StatCardProps) {
  return (
    <div className={`card-theme stat-card ${className}`}>
      <div className="stat-card-icon">
        {icon}
      </div>

      <div className="stat-card-content">
        <p className="stat-card-title">
          {title}
        </p>

        <h3 className="stat-card-value">
          {value}
        </h3>
      </div>
    </div>
  );
}