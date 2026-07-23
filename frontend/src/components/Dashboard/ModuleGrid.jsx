import ModuleCard from "./ModuleCard";

const modules = [
  {
    title: "Resume Analyzer",
    emoji: "📄",
    path: "/resume",
    description: "Analyze ATS score and improve resumes.",
  },
  {
    title: "PDF Summarizer",
    emoji: "📚",
    path: "/pdf",
    description: "Summarize long PDF documents instantly.",
  },
  {
    title: "Video Summarizer",
    emoji: "🎥",
    path: "/video",
    description: "Generate summaries from videos.",
  },
  {
    title: "Audio Summarizer",
    emoji: "🎧",
    path: "/audio",
    description: "Convert speech into summarized notes.",
  },
  {
    title: "Text Summarizer",
    emoji: "📝",
    path: "/text",
    description: "Summarize long articles and documents.",
  },
];

const ModuleGrid = () => {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
      {modules.map((module) => (
        <ModuleCard key={module.title} {...module} />
      ))}
    </div>
  );
};

export default ModuleGrid;