import ModuleCard from "./ModuleCard";

const modules = [
  {
    title: "Resume Analyzer",
    description: "Improve your resume with AI-powered ATS analysis.",
    emoji: "📄",
  },
  {
    title: "PDF Summarizer",
    description: "Summarize long PDFs in seconds.",
    emoji: "📕",
  },
  {
    title: "Video Summarizer",
    description: "Extract important points from videos.",
    emoji: "🎥",
  },
  {
    title: "Audio Summarizer",
    description: "Convert speech into concise summaries.",
    emoji: "🎙️",
  },
  {
    title: "Text Summarizer",
    description: "Generate smart summaries from text.",
    emoji: "📝",
  },
];

const Modules = () => {
  return (
    <section className="bg-[#09090B] py-24 px-6">
      <div className="max-w-7xl mx-auto">

        <h2 className="text-5xl font-bold text-center text-white">
          Our AI Modules
        </h2>

        <p className="mt-4 text-center text-gray-400 max-w-2xl mx-auto">
          Everything you need in one intelligent platform.
        </p>

        <div className="mt-16 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {modules.map((module, index) => (
            <ModuleCard
              key={index}
              title={module.title}
              description={module.description}
              emoji={module.emoji}
            />
          ))}
        </div>

      </div>
    </section>
  );
};

export default Modules;