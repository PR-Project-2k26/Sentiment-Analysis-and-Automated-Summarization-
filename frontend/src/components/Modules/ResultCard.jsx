const ResultCard = ({ title, children }) => {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
      <h2 className="mb-4 text-xl font-bold text-white">
        {title}
      </h2>

      {children}
    </div>
  );
};

export default ResultCard;