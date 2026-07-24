import { useEffect, useState } from "react";

import DashboardLayout from "../../components/Layout/DashboardLayout";

import Welcome from "../../components/Dashboard/Welcome";
import StatsGrid from "../../components/Dashboard/StatsGrid";
import ModuleGrid from "../../components/Dashboard/ModuleGrid";
import RecentActivity from "../../components/Dashboard/RecentActivity";

import { getDashboardStats } from "../../services/dashboardService";

const Dashboard = () => {
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);

  // Logged-in user
  const user = JSON.parse(localStorage.getItem("user"));

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
        <div className="flex h-96 items-center justify-center text-gray-400">
          Loading Dashboard...
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="space-y-8">
        <Welcome user={user} />

        <StatsGrid stats={dashboardData} />

        <ModuleGrid />

        <RecentActivity
          activities={dashboardData?.recentActivity || []}
        />
      </div>
    </DashboardLayout>
  );
};

export default Dashboard;