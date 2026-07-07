import "./../../styles/sidebar.css";

import { NavLink } from "react-router-dom";

import {
  LayoutDashboard,
  MessageCircle,
  Brain,
  Smile,
  Users,
  BarChart3,
  History,
  Settings,
  ClipboardList,
} from "lucide-react";

interface SidebarProps {
  sidebarOpen: boolean;
}

const menuItems = [
  {
    to: "/",
    label: "Dashboard",
    icon: LayoutDashboard,
  },
  {
    to: "/chat",
    label: "Chat",
    icon: MessageCircle,
  },
  {
    to: "/memory",
    label: "Memory",
    icon: Brain,
  },
  {
    to: "/mood",
    label: "Mood",
    icon: Smile,
  },
  {
    to: "/personality",
    label: "Personality",
    icon: Users,
  },
  {
    to: "/survey",
    label: "Survey",
    icon: ClipboardList,
  },
  {
    to: "/analytics",
    label: "Analytics",
    icon: BarChart3,
  },
  {
    to: "/history",
    label: "History",
    icon: History,
  },
  {
    to: "/settings",
    label: "Settings",
    icon: Settings,
  },
];

export default function Sidebar({ sidebarOpen }: SidebarProps) {
  return (
    <aside className={sidebarOpen ? "sidebar open" : "sidebar"}>
      <div className="sidebar-logo">
        <h3>Project-60</h3>
      </div>

      <nav>
        {menuItems.map((item) => {
          const Icon = item.icon;

          return (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.to === "/"}
              className={({ isActive }) =>
                isActive ? "sidebar-link active" : "sidebar-link"
              }
            >
              <Icon size={20} />
              <span>{item.label}</span>
            </NavLink>
          );
        })}
      </nav>
    </aside>
  );
}
