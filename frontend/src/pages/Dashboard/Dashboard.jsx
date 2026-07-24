import { useEffect, useState } from "react";

import DashboardLayout from "../../components/Layout/DashboardLayout";

import Welcome from "../../components/Dashboard/Welcome";
import StatsGrid from "../../components/Dashboard/StatsGrid";
import ModuleGrid from "../../components/Dashboard/ModuleGrid";
import UsageChart from "../../components/Dashboard/UsageChart";
import QuickActions from "../../components/Dashboard/QuickActions";
import RecentActivity from "../../components/Dashboard/RecentActivity";

import { getDashboardStats } from "../../services/dashboardService";

const Dashboard = () => {
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const response = await getDashboardStats();
        setDashboardData(response.data);
      } catch (error) {
        console.error("Dashboard Error:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, []);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="flex items-center justify-center h-96 text-gray-400">
          Loading Dashboard...
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="space-y-8">
        <Welcome />

        <StatsGrid stats={dashboardData} />

        <div className="grid gap-8 xl:grid-cols-3">
          <div className="space-y-8 xl:col-span-2">
            <ModuleGrid />

            <UsageChart stats={dashboardData} />
          </div>

          <div className="space-y-8">
            <QuickActions />

            <RecentActivity
              activities={dashboardData?.recentActivity || []}
            />
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
};

export default Dashboard;