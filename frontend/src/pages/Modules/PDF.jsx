import { useState } from "react";

import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";
import ResultCard from "../../components/Modules/ResultCard";

import { summarizePDF } from "../../services/pdfService";

const PDF = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSummarize = async () => {
    if (!selectedFile) {
      alert("Please select a PDF.");
      return;
    }

    try {
      setLoading(true);

      const response = await summarizePDF(selectedFile);

      setResult(response);

    } catch (error) {
      console.error(error);

      alert(
        error?.response?.data?.message ||
        "Failed to summarize PDF."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <ModuleLayout
      title="PDF Summarizer"
      description="Upload a PDF and generate an AI-powered summary."
    >
      <FileUploadBox
        selectedFile={selectedFile}
        onFileSelect={setSelectedFile}
        accept=".pdf"
        title="Drag & Drop your PDF"
      />

      <button
        onClick={handleSummarize}
        disabled={loading}
        className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Summarizing..." : "Summarize PDF"}
      </button>

      <div className="mt-8">
        <ResultCard title="Summary">
          {result ? (
            <>
              <p className="mb-4 text-sm text-gray-400">
                <strong>File:</strong> {result.filename}
              </p>

              <p className="mb-4 text-sm text-gray-400">
                <strong>Characters:</strong> {result.characters}
              </p>

              <p className="whitespace-pre-wrap text-gray-300">
                {result.summary}
              </p>
            </>
          ) : (
            <p className="text-gray-400">
              Upload a PDF to generate a summary.
            </p>
          )}
        </ResultCard>
      </div>
    </ModuleLayout>
  );
};

export default PDF;