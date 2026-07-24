import { useState } from "react";

import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";
import ResultCard from "../../components/Modules/ResultCard";

import { uploadAudio } from "../../services/audioService";

const Audio = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select an audio file.");
      return;
    }

    try {
      setLoading(true);

      const response = await uploadAudio(selectedFile);

      setResult(response);
    } catch (error) {
      console.error(error);

      alert(
        error?.response?.data?.message ||
          "Failed to summarize the audio."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <ModuleLayout
      title="Audio Summarizer"
      description="Upload an audio file to generate a transcript and summary."
    >
      <FileUploadBox
        selectedFile={selectedFile}
        onFileSelect={setSelectedFile}
        accept=".mp3,.wav,.m4a,.aac"
        title="Drag & Drop your Audio"
        icon="🎵"
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Summarizing..." : "Summarize Audio"}
      </button>

      <div className="mt-8 space-y-6">
        <ResultCard title="Transcript">
          {result ? (
            <p className="whitespace-pre-wrap text-gray-300">
              {result.transcript}
            </p>
          ) : (
            <p className="text-gray-400">
              Upload an audio file to view its transcript.
            </p>
          )}
        </ResultCard>

        <ResultCard title="Audio Summary">
          {result ? (
            <p className="whitespace-pre-wrap text-gray-300">
              {result.summary}
            </p>
          ) : (
            <p className="text-gray-400">
              Upload an audio file to generate a summary.
            </p>
          )}
        </ResultCard>
      </div>
    </ModuleLayout>
  );
};

export default Audio;