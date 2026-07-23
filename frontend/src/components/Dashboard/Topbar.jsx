import { useNavigate } from "react-router-dom";

const Topbar = ({ user }) => {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  return (
    <div className="flex items-center justify-between border-b border-white/10 pb-5">
      <input
        placeholder="Search modules..."
        className="w-96 rounded-xl border border-white/10 bg-white/5 px-4 py-3 text-white outline-none"
      />

      <div className="flex items-center gap-4">
        <div className="text-right">
          <p className="font-semibold">
            {user?.name || "User"}
          </p>

          <p className="text-sm text-gray-400">
            {user?.email || ""}
          </p>
        </div>

        <button
          onClick={logout}
          className="rounded-xl bg-red-600 px-4 py-2 text-white transition hover:bg-red-700"
        >
          Logout
        </button>
      </div>
    </div>
  );
};

export default Topbar;