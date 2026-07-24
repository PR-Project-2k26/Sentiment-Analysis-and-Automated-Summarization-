import { NavLink, useNavigate } from "react-router-dom";
import {
  LayoutDashboard,
  History,
  FileText,
  File,
  Video,
  Headphones,
  Type,
  User,
  Settings,
  LogOut,
} from "lucide-react";

const links = [
  {
    section: "General",
    items: [
      {
        name: "Dashboard",
        path: "/dashboard",
        icon: LayoutDashboard,
      },
      {
        name: "History",
        path: "/history",
        icon: History,
      },
    ],
  },
  {
    section: "AI Modules",
    items: [
      {
        name: "Resume",
        path: "/resume",
        icon: FileText,
      },
      {
        name: "PDF",
        path: "/pdf",
        icon: File,
      },
      {
        name: "Video",
        path: "/video",
        icon: Video,
      },
      {
        name: "Audio",
        path: "/audio",
        icon: Headphones,
      },
      {
        name: "Text",
        path: "/text",
        icon: Type,
      },
    ],
  },
  {
    section: "Account",
    items: [
      {
        name: "Profile",
        path: "/profile",
        icon: User,
      },
      {
        name: "Settings",
        path: "/settings",
        icon: Settings,
      },
    ],
  },
];

const Sidebar = () => {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  return (
    <aside className="flex min-h-screen w-64 flex-col border-r border-white/10 bg-[#0E1016] p-6">

      {/* Logo */}
      <h1 className="mb-10 text-3xl font-bold text-white">
        Summar<span className="text-blue-500">AI</span>
      </h1>

      {/* Navigation */}
      <nav className="flex-1 space-y-8">

        {links.map((section) => (
          <div key={section.section}>

            <p className="mb-3 px-2 text-xs font-semibold uppercase tracking-wider text-gray-500">
              {section.section}
            </p>

            <div className="space-y-2">

              {section.items.map((link) => {
                const Icon = link.icon;

                return (
                  <NavLink
                    key={link.name}
                    to={link.path}
                    className={({ isActive }) =>
                      `flex items-center gap-3 rounded-xl px-4 py-3 transition-all ${
                        isActive
                          ? "bg-blue-600 text-white shadow-md"
                          : "text-gray-400 hover:bg-white/5 hover:text-white"
                      }`
                    }
                  >
                    <Icon size={18} />
                    <span>{link.name}</span>
                  </NavLink>
                );
              })}

            </div>

          </div>
        ))}

      </nav>

      {/* Logout */}

      <div className="border-t border-white/10 pt-5">

        <button
          onClick={logout}
          className="flex w-full items-center gap-3 rounded-xl px-4 py-3 text-red-400 transition hover:bg-red-500/10 hover:text-red-300"
        >
          <LogOut size={18} />
          Logout
        </button>

      </div>

    </aside>
  );
};

export default Sidebar;