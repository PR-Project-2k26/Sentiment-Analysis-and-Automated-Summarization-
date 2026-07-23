import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";
import ResultCard from "../../components/Modules/ResultCard";

const Audio = () => {
  return (
    <ModuleLayout
      title="Audio Summarizer"
      description="Upload an audio file to generate a transcript and summary."
    >
      <FileUploadBox />

      <button className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700">
        Summarize Audio
      </button>

      <div className="mt-8">
        <ResultCard title="Audio Summary">
          <p className="text-gray-400">
            Upload an audio file to generate a summary.
          </p>
        </ResultCard>
      </div>
    </ModuleLayout>
  );
};

export default Audio;