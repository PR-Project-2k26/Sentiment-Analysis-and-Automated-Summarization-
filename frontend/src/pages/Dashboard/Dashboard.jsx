import { useEffect, useState } from "react";

import Sidebar from "../../components/Dashboard/Sidebar";
import Topbar from "../../components/Dashboard/Topbar";
import Welcome from "../../components/Dashboard/Welcome";
import StatsGrid from "../../components/Dashboard/StatsGrid";
import ModuleGrid from "../../components/Dashboard/ModuleGrid";
import UsageChart from "../../components/Dashboard/UsageChart";
import QuickActions from "../../components/Dashboard/QuickActions";
import RecentActivity from "../../components/Dashboard/RecentActivity";

import { getProfile } from "../../services/dashboardService";

const Dashboard = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await getProfile();
        setUser(response.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchProfile();
  }, []);

  return (
    <div className="flex min-h-screen bg-[#09090B] text-white">
      <Sidebar />

      <main className="flex-1 overflow-y-auto p-8">
        <Topbar user={user} />

        <div className="mt-8 space-y-8">
          <Welcome user={user} />

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
      </main>
    </div>
  );
};

export default Dashboard;