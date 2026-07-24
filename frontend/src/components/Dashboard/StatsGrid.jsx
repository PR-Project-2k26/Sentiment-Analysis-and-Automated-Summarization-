import StatsCard from "./StatsCard";

const StatsGrid = ({ stats }) => {
  const dashboardStats = [
    {
      //emoji: "📊",
      title: "Total Analyses",
      value: stats?.totalAnalyses || 0,
    },
    {
      //emoji: "📄",
      title: "Resume",
      value: stats?.resume || 0,
    },
    {
      //emoji: "📚",
      title: "PDF",
      value: stats?.pdf || 0,
    },
    {
      //emoji: "🎥",
      title: "Video",
      value: stats?.video || 0,
    },
    {
      //emoji: "🎧",
      title: "Audio",
      value: stats?.audio || 0,
    },
    {
      //emoji: "📝",
      title: "Text",
      value: stats?.text || 0,
    },
  ];

  return (
    <div className="mb-8 grid grid-cols-2 gap-4 md:grid-cols-3 xl:grid-cols-6">
      {dashboardStats.map((item) => (
        <StatsCard key={item.title} {...item} />
      ))}
    </div>
  );
};

export default StatsGrid;