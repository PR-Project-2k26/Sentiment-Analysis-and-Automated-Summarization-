import { useEffect, useState } from "react";
import Sidebar from "../Dashboard/Sidebar";
import Topbar from "../Dashboard/Topbar";
import { getProfile } from "../../services/dashboardService";

const DashboardLayout = ({ children }) => {
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

        <div className="mt-8">{children}</div>
      </main>
    </div>
  );
};

export default DashboardLayout;