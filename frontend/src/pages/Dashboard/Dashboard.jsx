import Sidebar from "../../components/Dashboard/Sidebar";
import Topbar from "../../components/Dashboard/Topbar";
import Welcome from "../../components/Dashboard/Welcome";
import ModuleGrid from "../../components/Dashboard/ModuleGrid";

const Dashboard = () => {
  return (
    <div className="flex min-h-screen bg-[#09090B]">
      <Sidebar />

      <main className="flex-1 p-10">
        <Topbar />

        <div className="mt-10">
          <Welcome />
          <ModuleGrid />
        </div>
      </main>
    </div>
  );
};

export default Dashboard;