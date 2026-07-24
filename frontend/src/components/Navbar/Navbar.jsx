import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  const handleGetStarted = () => {
    if (token) {
      navigate("/dashboard");
    } else {
      navigate("/login");
    }
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    navigate("/");
  };

  return (
    <nav className="fixed top-0 left-0 z-50 w-full border-b border-white/10 bg-[#09090B]/90 backdrop-blur-lg">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">

        {/* Logo */}

        <Link
          to="/"
          className="text-2xl font-bold text-white"
        >
          AI <span className="text-blue-500">Summarizer</span>
        </Link>

        {/* Center Links */}

        <div className="hidden items-center gap-8 md:flex">

          <a
            href="#modules"
            className="text-gray-300 transition hover:text-white"
          >
            Modules
          </a>

          <a
            href="#architecture"
            className="text-gray-300 transition hover:text-white"
          >
            How It Works
          </a>

          <a
            href="#team"
            className="text-gray-300 transition hover:text-white"
          >
            Team
          </a>

        </div>

        {/* Right Side */}

        {!token ? (
          <div className="flex items-center gap-4">

            <button
              onClick={() => navigate("/login")}
              className="text-gray-300 transition hover:text-white"
            >
              Login
            </button>

            <button
              onClick={() => navigate("/register")}
              className="rounded-xl bg-blue-600 px-5 py-2 font-medium text-white transition hover:bg-blue-700"
            >
              Register
            </button>

          </div>
        ) : (
          <div className="flex items-center gap-4">

            <button
              onClick={() => navigate("/dashboard")}
              className="text-gray-300 transition hover:text-white"
            >
              Dashboard
            </button>

            <button
              onClick={() => navigate("/history")}
              className="text-gray-300 transition hover:text-white"
            >
              History
            </button>

            <button
              onClick={handleLogout}
              className="rounded-xl bg-red-600 px-4 py-2 text-white transition hover:bg-red-700"
            >
              Logout
            </button>

          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;