import ModuleLayout from "../../layouts/ModuleLayout";
import ResultCard from "../../components/Modules/ResultCard";

const Text = () => {
  return (
    <ModuleLayout
      title="Text Summarizer"
      description="Paste text and generate an AI-powered summary."
    >
      <textarea
        rows={10}
        placeholder="Paste your text here..."
        className="w-full rounded-2xl border border-white/10 bg-white/5 p-5 text-white outline-none focus:border-blue-500"
      />

      <button className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700">
        Summarize Text
      </button>

      <div className="mt-8">
        <ResultCard title="Summary">
          <p className="text-gray-400">
            Enter some text to generate a summary.
          </p>
        </ResultCard>
      </div>
    </ModuleLayout>
  );
};

export default Text;