const RecentActivity = ({ activities }) => {
  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
      <h2 className="mb-6 text-2xl font-bold text-white">
        Recent Activity
      </h2>

      {activities.length === 0 ? (
        <div className="py-8 text-center text-gray-400">
          No recent activity found.
        </div>
      ) : (
        <div className="space-y-5">
          {activities.map((activity) => (
            <div
              key={activity.id}
              className="flex items-center justify-between border-b border-white/10 pb-4 last:border-none"
            >
              <div>
                <p className="font-medium text-white">
                  {activity.module}
                </p>

                <p className="text-sm text-gray-400">
                  {activity.file_name}
                </p>

                <p className="text-xs text-gray-500 mt-1">
                  {new Date(activity.created_at).toLocaleString()}
                </p>
              </div>

              <div className="text-xl text-green-400">
                ✔
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default RecentActivity;