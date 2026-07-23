import { NavLink } from "react-router-dom";

const links = [
  { name: "Dashboard", path: "/dashboard" },
  { name: "Resume", path: "/resume" },
  { name: "PDF", path: "/pdf" },
  { name: "Video", path: "/video" },
  { name: "Audio", path: "/audio" },
  { name: "Text", path: "/text" },
  { name: "Profile", path: "/profile" },
  { name: "Settings", path: "/settings" },
];

const Sidebar = () => {
  return (
    <aside className="w-64 min-h-screen border-r border-white/10 bg-[#0E1016] p-6">
      <h1 className="mb-10 text-3xl font-bold text-white">
        Summar<span className="text-blue-500">AI</span>
      </h1>

      <nav className="space-y-2">
        {links.map((link) => (
          <NavLink
            key={link.name}
            to={link.path}
            className={({ isActive }) =>
              `block rounded-xl px-4 py-3 transition ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-gray-400 hover:bg-white/5 hover:text-white"
              }`
            }
          >
            {link.name}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;