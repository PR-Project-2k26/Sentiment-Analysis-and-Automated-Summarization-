const StatsCard = ({ emoji, title, value }) => {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-5 transition-all duration-300 hover:-translate-y-1 hover:border-blue-500 hover:bg-white/10">
      <div className="text-3xl">{emoji}</div>

      <h3 className="mt-3 text-base font-medium text-gray-300">
        {title}
      </h3>

      <p className="mt-2 text-3xl font-bold text-white">
        {value}
      </p>
    </div>
  );
};

export default StatsCard;