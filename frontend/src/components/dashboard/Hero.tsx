import "./../../styles/dashboard/hero.css";

import { MessageCircle } from "lucide-react";

export default function Hero() {
  const hour = new Date().getHours();

  let greeting = "Good Evening";

  if (hour < 12) {
    greeting = "Good Morning";
  } else if (hour < 18) {
    greeting = "Good Afternoon";
  }

  return (
    <section className="hero card-theme">
      <div className="hero-content">
        <div>
          <span className="hero-greeting">{greeting}, Neil 👋</span>

          <h1 className="hero-title">Project-60</h1>

          <p className="hero-description">
            Your AI companion that grows with you.
          </p>
        </div>

        <button className="hero-button">
          <MessageCircle size={18} />
          <span>Start Chat</span>
        </button>
      </div>
    </section>
  );
}
