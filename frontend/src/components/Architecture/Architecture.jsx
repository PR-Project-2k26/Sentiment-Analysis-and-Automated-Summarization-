const steps = [
  {
    title: "Upload",
    description: "Upload a PDF, resume, video, audio, or text document.",
    emoji: "📤",
  },
  {
    title: "AI Processing",
    description: "Our AI analyzes and processes the uploaded content.",
    emoji: "🤖",
  },
  {
    title: "Generate Results",
    description: "Receive summaries, insights, ATS scores, or transcripts.",
    emoji: "⚡",
  },
];

const Architecture = () => {
  return (
    <section id="architecture" className="bg-[#09090B] py-24 px-6">
      <div className="max-w-7xl mx-auto">

        <div className="text-center">
          <h2 className="text-5xl font-bold text-white">
            How It Works
          </h2>

          <p className="mt-4 text-gray-400">
            A simple three-step workflow powered by AI.
          </p>
        </div>

        <div className="mt-16 grid md:grid-cols-3 gap-8">
          {steps.map((step, index) => (
            <div
              key={index}
              className="rounded-2xl border border-white/10 bg-white/5 p-8 text-center hover:border-blue-500/40 transition"
            >
              <div className="text-6xl">{step.emoji}</div>

              <h3 className="mt-6 text-2xl font-bold text-white">
                {step.title}
              </h3>

              <p className="mt-4 text-gray-400">
                {step.description}
              </p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
};

export default Architecture;