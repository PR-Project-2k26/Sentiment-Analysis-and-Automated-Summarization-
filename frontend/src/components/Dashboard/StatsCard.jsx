const StatsCard = ({ emoji, title, value }) => {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6 transition-all duration-300 hover:-translate-y-1 hover:border-blue-500 hover:bg-white/10">
      <div className="text-4xl">{emoji}</div>

      <h3 className="mt-4 text-lg font-semibold text-gray-300">
        {title}
      </h3>

      <p className="mt-3 text-4xl font-bold text-white">
        {value}
      </p>
    </div>
  );
};

export default StatsCard;