import QuickActionCard from "./QuickActionCard";

const actions = [
  {
    emoji: "📄",
    title: "Analyze Resume",
    path: "/resume",
  },
  {
    emoji: "📚",
    title: "Upload PDF",
    path: "/pdf",
  },
  {
    emoji: "🎥",
    title: "Summarize Video",
    path: "/video",
  },
  {
    emoji: "🎧",
    title: "Transcribe Audio",
    path: "/audio",
  },
];

const QuickActions = () => {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">

      <h2 className="mb-6 text-2xl font-bold text-white">
        ⚡ Quick Actions
      </h2>

      <div className="space-y-4">
        {actions.map((action) => (
          <QuickActionCard
            key={action.title}
            {...action}
          />
        ))}
      </div>

    </div>
  );
};

export default QuickActions;