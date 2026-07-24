import { useState } from "react";

import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";
import ResultCard from "../../components/Modules/ResultCard";

import { uploadVideo } from "../../services/videoService";

const Video = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a video.");
      return;
    }

    try {
      setLoading(true);

      const response = await uploadVideo(selectedFile);

      setResult(response);
    } catch (error) {
      console.error(error);

      alert(
        error?.response?.data?.message ||
          "Failed to summarize the video."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <ModuleLayout
      title="Video Summarizer"
      description="Upload a video and generate an AI-powered summary."
    >
      <FileUploadBox
      selectedFile={selectedFile}
      onFileSelect={setSelectedFile}
      accept=".mp4,.mov,.avi,.mkv"
      title="Drag & Drop your Video"
      icon="🎥"
    />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Summarizing..." : "Summarize Video"}
      </button>

      <div className="mt-8 space-y-6">
        <ResultCard title="Transcript">
          {result ? (
            <p className="whitespace-pre-wrap text-gray-300">
              {result.transcript}
            </p>
          ) : (
            <p className="text-gray-400">
              Upload a video to view its transcript.
            </p>
          )}
        </ResultCard>

        <ResultCard title="Video Summary">
          {result ? (
            <p className="whitespace-pre-wrap text-gray-300">
              {result.summary}
            </p>
          ) : (
            <p className="text-gray-400">
              Upload a video to generate a summary.
            </p>
          )}
        </ResultCard>
      </div>
    </ModuleLayout>
  );
};

export default Video;