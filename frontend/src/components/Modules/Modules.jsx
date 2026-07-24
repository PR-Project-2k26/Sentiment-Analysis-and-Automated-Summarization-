import ModuleCard from "./ModuleCard";

const modules = [
  {
    title: "Resume Analyzer",
    description:
      "Improve your resume with AI-powered ATS analysis and suggestions.",
    link: "/resume",
  },
  {
    title: "PDF Summarizer",
    description:
      "Summarize long PDF documents into concise notes instantly.",
    link: "/pdf",
  },
  {
    title: "Video Summarizer",
    description:
      "Extract key highlights and summaries from videos.",
    link: "/video",
  },
  {
    title: "Audio Summarizer",
    description:
      "Convert speech into text and generate smart summaries.",
    link: "/audio",
  },
  {
    title: "Text Summarizer",
    description:
      "Generate concise summaries from long text using AI.",
    link: "/text",
  },
];

const Modules = () => {
  return (
    <section id="modules" className="bg-[#09090B] px-6 py-24">
      <div className="mx-auto max-w-7xl">

        {/* Heading */}
        <div className="text-center">
          <h2 className="text-5xl font-bold text-white">
            Our AI Modules
          </h2>

          <p className="mx-auto mt-4 max-w-2xl text-lg text-gray-400">
            Access multiple AI-powered tools from one unified platform.
            Choose any module to get started.
          </p>
        </div>

        {/* Cards */}
        <div className="mt-16 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {modules.map((module, index) => (
            <ModuleCard
              key={index}
              title={module.title}
              description={module.description}
              link={module.link}
            />
          ))}
        </div>

      </div>
    </section>
  );
};

export default Modules;