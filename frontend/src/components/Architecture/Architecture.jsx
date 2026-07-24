const steps = [
  {
    title: "Upload",
    description: "Upload a PDF, resume, video, audio, or text document.",
  },
  {
    title: "AI Processing",
    description: "Our AI analyzes and processes the uploaded content.",
  },
  {
    title: "Generate Results",
    description: "Receive summaries, insights, ATS scores, or transcripts.",
  },
];

const Architecture = () => {
  return (
    <section id="architecture" className="bg-[#09090B] py-24 px-6">
      <div className="mx-auto max-w-7xl">

        <div className="text-center">
          <h2 className="text-5xl font-bold text-white">
            How It Works
          </h2>

          <p className="mt-4 text-gray-400">
            A simple three-step workflow powered by AI.
          </p>
        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-3">
          {steps.map((step, index) => (
            <div
              key={index}
              className="rounded-2xl border border-white/10 bg-white/5 p-8 text-center transition hover:border-blue-500/40"
            >
              <h3 className="text-2xl font-bold text-white">
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