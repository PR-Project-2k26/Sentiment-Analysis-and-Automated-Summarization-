import Sidebar from "../Dashboard/Sidebar";
import Topbar from "../Dashboard/Topbar";

const DashboardLayout = ({ children }) => {
  return (
    <div className="flex min-h-screen bg-[#09090B] text-white">
      <Sidebar />

      <main className="flex-1 overflow-y-auto p-8">
        <Topbar />

        <div className="mt-8">{children}</div>
      </main>
    </div>
  );
};

export default DashboardLayout;