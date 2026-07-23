const activities = [
  {
    title: "Resume analyzed",
    time: "2 minutes ago",
  },
  {
    title: "PDF summarized",
    time: "Today",
  },
  {
    title: "Video summarized",
    time: "Yesterday",
  },
  {
    title: "Audio transcription completed",
    time: "2 days ago",
  },
];

const RecentActivity = () => {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
      <h2 className="mb-6 text-2xl font-bold text-white">
        Recent Activity
      </h2>

      <div className="space-y-5">
        {activities.map((activity, index) => (
          <div
            key={index}
            className="flex items-center justify-between border-b border-white/10 pb-4 last:border-none"
          >
            <div>
              <p className="font-medium text-white">
                {activity.title}
              </p>

              <p className="text-sm text-gray-400">
                {activity.time}
              </p>
            </div>

            <div className="text-green-400 text-xl">
              ✔
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecentActivity;