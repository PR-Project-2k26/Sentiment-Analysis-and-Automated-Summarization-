const HeroScore = ({ result }) => {
  if (!result) return null;

  const score = result.resumeScore;

  let title = "";
  let color = "";

  if (score >= 90) {
    title = "🟢 Excellent Resume";
    color = "bg-green-500";
  } else if (score >= 75) {
    title = "🔵 Good Resume";
    color = "bg-blue-500";
  } else if (score >= 60) {
    title = "🟡 Average Resume";
    color = "bg-yellow-500";
  } else {
    title = "🔴 Needs Improvement";
    color = "bg-red-500";
  }

  return (
    <div className="space-y-8">

      {/* Hero Card */}
      <div className={`${color} rounded-3xl p-10 text-center shadow-2xl`}>

        <h1 className="text-6xl font-extrabold">
          {score}/100
        </h1>

        <p className="mt-5 text-3xl font-semibold">
          {title}
        </p>

      </div>

      {/* Metrics */}
      <div className="grid grid-cols-2 gap-6 md:grid-cols-4">

        <div className="rounded-2xl border border-white/10 bg-white/5 p-5 text-center">
          <p className="text-gray-400">🎯 ATS</p>

          <h2 className="mt-2 text-3xl font-bold">
            {result.atsScore}/20
          </h2>
        </div>

        <div className="rounded-2xl border border-white/10 bg-white/5 p-5 text-center">
          <p className="text-gray-400">💼 Job Match</p>

          <h2 className="mt-2 text-3xl font-bold">
            {result.skillScore}/40
          </h2>
        </div>

        <div className="rounded-2xl border border-white/10 bg-white/5 p-5 text-center">
          <p className="text-gray-400">📝 Content</p>

          <h2 className="mt-2 text-3xl font-bold">
            {result.scoreBreakdown?.["Content Quality"] ?? 0}/20
          </h2>
        </div>

        <div className="rounded-2xl border border-white/10 bg-white/5 p-5 text-center">
          <p className="text-gray-400">📄 Structure</p>

          <h2 className="mt-2 text-3xl font-bold">
            {result.scoreBreakdown?.["Resume Structure"] ?? 0}/20
          </h2>
        </div>

      </div>

    </div>
  );
};

export default HeroScore;