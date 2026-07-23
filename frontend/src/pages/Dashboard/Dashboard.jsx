import Sidebar from "../../components/Dashboard/Sidebar";
import Topbar from "../../components/Dashboard/Topbar";
import Welcome from "../../components/Dashboard/Welcome";
import StatsGrid from "../../components/Dashboard/StatsGrid";
import ModuleGrid from "../../components/Dashboard/ModuleGrid";
import QuickActions from "../../components/Dashboard/QuickActions";
import RecentActivity from "../../components/Dashboard/RecentActivity";

const Dashboard = () => {
  return (
    <div className="flex min-h-screen bg-[#09090B]">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content */}
      <main className="flex-1 p-8 overflow-y-auto">
        {/* Top Navigation */}
        <Topbar />

        {/* Dashboard Content */}
        <div className="mt-8 space-y-8">
          {/* Welcome Section */}
          <Welcome />

          {/* Statistics */}
          <StatsGrid />

          {/* Modules + Right Panel */}
          <div className="grid gap-8 xl:grid-cols-3">
            {/* AI Modules */}
            <div className="xl:col-span-2">
              <ModuleGrid />
            </div>

            {/* Right Sidebar */}
            <div className="space-y-8">
              <QuickActions />
              <RecentActivity />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;