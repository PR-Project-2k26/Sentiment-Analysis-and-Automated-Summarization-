import { Link } from "react-router-dom";

const ModuleCard = ({ title, description, path, emoji }) => {
  return (
    <Link
      to={path}
      className="rounded-2xl border border-white/10 bg-white/5 p-6 transition duration-300 hover:-translate-y-2 hover:border-blue-500 hover:bg-white/10"
    >
      <div className="text-4xl">{emoji}</div>

      <h2 className="mt-5 text-2xl font-bold text-white">
        {title}
      </h2>

      <p className="mt-3 text-gray-400">
        {description}
      </p>
    </Link>
  );
};

export default ModuleCard;