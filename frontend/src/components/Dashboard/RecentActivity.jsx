const RecentActivity = ({ activities }) => {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
      <h2 className="mb-5 text-2xl font-bold text-white">
        Recent Activity
      </h2>

      {activities.length === 0 ? (
        <div className="py-8 text-center text-gray-400">
          No recent activity found.
        </div>
      ) : (
        <div className="divide-y divide-white/10">
          {activities.map((activity) => (
            <div
              key={activity.id}
              className="flex items-start justify-between py-4"
            >
              {/* Left */}
              <div className="min-w-0">
                <p className="font-semibold text-white">
                  {activity.module}
                </p>

                <p className="mt-1 truncate text-sm text-gray-400">
                  {activity.file_name}
                </p>
              </div>

              {/* Right */}
              <div className="ml-6 flex items-center gap-3 whitespace-nowrap">
                <p className="text-sm text-gray-500">
                  {new Date(activity.created_at).toLocaleDateString("en-GB", {
                    day: "2-digit",
                    month: "short",
                    year: "numeric",
                  })}{" "}
                  •{" "}
                  {new Date(activity.created_at).toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit",
                  })}
                </p>

                <span className="text-lg text-green-400"></span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default RecentActivity;