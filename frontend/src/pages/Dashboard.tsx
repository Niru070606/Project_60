import Hero from "../components/dashboard/Hero";
import StatsGrid from "../components/dashboard/StatsGrid";
import RecentActivity from "../components/dashboard/RecentActivity";
import QuickActions from "../components/dashboard/QuickActions";
import AIStatus from "../components/dashboard/AIStatus";


export default function Dashboard() {
  return (
    <div className="dashboard-container">
      <Hero />

      <section className="dashboard-section">
        <StatsGrid />
      </section>

      <section className="dashboard-section">
        <RecentActivity />
      </section>

      <section className="dashboard-section">
        <QuickActions />
      </section>

      <section className="dashboard-section">
        <AIStatus />
      </section>
    </div>
  );
}