import { Link } from "react-router-dom";

const QuickActionCard = ({ emoji, title, path }) => {
  return (
    <Link
      to={path}
      className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 p-5 transition duration-300 hover:border-blue-500 hover:bg-white/10"
    >
      <div className="flex items-center gap-4">
        <span className="text-3xl">{emoji}</span>

        <div>
          <h3 className="font-semibold text-white">
            {title}
          </h3>

          <p className="text-sm text-gray-400">
            Open module
          </p>
        </div>
      </div>

      <span className="text-gray-400 text-xl">
        →
      </span>
    </Link>
  );
};

export default QuickActionCard;