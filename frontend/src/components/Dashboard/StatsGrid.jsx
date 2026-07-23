import StatsCard from "./StatsCard";

const stats = [
  {
    emoji: "📄",
    title: "Resumes",
    value: 24,
  },
  {
    emoji: "📚",
    title: "PDFs",
    value: 18,
  },
  {
    emoji: "🎥",
    title: "Videos",
    value: 9,
  },
  {
    emoji: "🎧",
    title: "Audio",
    value: 12,
  },
];

const StatsGrid = () => {
  return (
    <div className="mb-10 grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {stats.map((item) => (
        <StatsCard key={item.title} {...item} />
      ))}
    </div>
  );
};

export default StatsGrid;