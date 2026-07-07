import "./../../styles/navbar.css";

import type { Dispatch, SetStateAction } from "react";

import ThemeToggle from "../common/ThemeToggle";

import { Bell, Menu, Search, User } from "lucide-react";

interface NavbarProps {
  sidebarOpen: boolean;
  setSidebarOpen: Dispatch<SetStateAction<boolean>>;
}

export default function Navbar({ sidebarOpen, setSidebarOpen }: NavbarProps) {
  return (
    <nav className="navbar-custom">
      <div className="navbar-left">
        <button
          className="icon-btn"
          onClick={() => setSidebarOpen(!sidebarOpen)}
        >
          <Menu size={22} />
        </button>

        <h4 className="logo">Project-60</h4>
      </div>

      <div className="navbar-center">
        <div className="search-box">
          <Search size={18} />
          <input type="text" placeholder="Search..." />
        </div>
      </div>

      <div className="navbar-right">
        <ThemeToggle />

        <button className="icon-btn">
          <Bell size={20} />
        </button>

        <button className="icon-btn">
          <User size={20} />
        </button>
      </div>
    </nav>
  );
}
