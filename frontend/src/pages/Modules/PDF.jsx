import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";
import ResultCard from "../../components/Modules/ResultCard";

const PDF = () => {
  return (
    <ModuleLayout
      title="PDF Summarizer"
      description="Upload a PDF and generate an AI-powered summary."
    >
      <FileUploadBox />

      <button className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold hover:bg-blue-700 transition">
        Summarize PDF
      </button>

      <div className="mt-8">
        <ResultCard title="Summary">
          <p className="text-gray-400">
            Upload a PDF to generate a summary.
          </p>
        </ResultCard>
      </div>
    </ModuleLayout>
  );
};

export default PDF;