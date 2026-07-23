import DashboardLayout from "../../components/Layout/DashboardLayout";

import Welcome from "../../components/Dashboard/Welcome";
import StatsGrid from "../../components/Dashboard/StatsGrid";
import ModuleGrid from "../../components/Dashboard/ModuleGrid";
import UsageChart from "../../components/Dashboard/UsageChart";
import QuickActions from "../../components/Dashboard/QuickActions";
import RecentActivity from "../../components/Dashboard/RecentActivity";

const Dashboard = () => {
  return (
    <DashboardLayout>
      <div className="space-y-8">
        <Welcome />

        <StatsGrid />

        <div className="grid gap-8 xl:grid-cols-3">
          <div className="space-y-8 xl:col-span-2">
            <ModuleGrid />
            <UsageChart />
          </div>

          <div className="space-y-8">
            <QuickActions />
            <RecentActivity />
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
};

export default Dashboard;