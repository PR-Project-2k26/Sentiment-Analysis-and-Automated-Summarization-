import Sidebar from "../../components/Dashboard/Sidebar";
import Topbar from "../../components/Dashboard/Topbar";
import Welcome from "../../components/Dashboard/Welcome";
import StatsGrid from "../../components/Dashboard/StatsGrid";
import ModuleGrid from "../../components/Dashboard/ModuleGrid";
import UsageChart from "../../components/Dashboard/UsageChart";
import QuickActions from "../../components/Dashboard/QuickActions";
import RecentActivity from "../../components/Dashboard/RecentActivity";

const Dashboard = () => {
  return (
    <div className="flex min-h-screen bg-[#09090B] text-white">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto p-8">
        {/* Top Navigation */}
        <Topbar />

        {/* Dashboard Content */}
        <div className="mt-8 space-y-8">
          {/* Welcome */}
          <Welcome />

          {/* Statistics Cards */}
          <StatsGrid />

          {/* Main Dashboard Grid */}
          <div className="grid gap-8 xl:grid-cols-3">
            {/* Left Section */}
            <div className="space-y-8 xl:col-span-2">
              {/* AI Modules */}
              <ModuleGrid />

              {/* Usage Analytics */}
              <UsageChart />
            </div>

            {/* Right Section */}
            <div className="space-y-8">
              {/* Quick Actions */}
              <QuickActions />

              {/* Recent Activity */}
              <RecentActivity />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;