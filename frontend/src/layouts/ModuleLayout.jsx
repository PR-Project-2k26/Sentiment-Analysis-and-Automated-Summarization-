import Sidebar from "../components/Dashboard/Sidebar";
import Topbar from "../components/Dashboard/Topbar";

const ModuleLayout = ({ title, description, children }) => {
  return (
    <div className="flex min-h-screen bg-[#09090B] text-white">
      <Sidebar />

      <main className="flex-1 overflow-y-auto p-8">
        <Topbar />

        <div className="mt-8">
          <h1 className="text-4xl font-bold">{title}</h1>

          <p className="mt-2 text-gray-400">
            {description}
          </p>

          <div className="mt-8">
            {children}
          </div>
        </div>
      </main>
    </div>
  );
};

export default ModuleLayout;