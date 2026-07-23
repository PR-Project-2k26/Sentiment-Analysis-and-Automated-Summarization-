const ModuleCard = ({ title, description, emoji }) => {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-md transition-all duration-300 hover:-translate-y-2 hover:border-blue-500/40 hover:bg-white/10">
      <div className="text-4xl">{emoji}</div>

      <h3 className="mt-5 text-2xl font-bold text-white">
        {title}
      </h3>

      <p className="mt-3 text-gray-400">
        {description}
      </p>

      <button className="mt-6 rounded-lg bg-blue-600 px-5 py-2 text-white hover:bg-blue-700 transition">
        Open Module →
      </button>
    </div>
  );
};

export default ModuleCard;