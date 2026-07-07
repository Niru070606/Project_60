import Hero from "../components/dashboard/Hero";
import StatsGrid from "../components/dashboard/StatsGrid";
import RecentActivity from "../components/dashboard/RecentActivity";
import QuickActions from "../components/dashboard/QuickActions";
import AIStatus from "../components/dashboard/AIStatus";


export default function Dashboard() {
  return (
    <div className="container-fluid">
      <Hero />
      <br />

      <StatsGrid />

      <RecentActivity />

      <QuickActions />

      <AIStatus />


    </div>
  );
}
