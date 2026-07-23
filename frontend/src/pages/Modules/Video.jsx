import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";
import ResultCard from "../../components/Modules/ResultCard";

const Video = () => {
  return (
    <ModuleLayout
      title="Video Summarizer"
      description="Upload a video and generate an AI-powered summary."
    >
      <FileUploadBox />

      <button className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700">
        Summarize Video
      </button>

      <div className="mt-8">
        <ResultCard title="Video Summary">
          <p className="text-gray-400">
            Upload a video to generate a summary.
          </p>
        </ResultCard>
      </div>
    </ModuleLayout>
  );
};

export default Video;