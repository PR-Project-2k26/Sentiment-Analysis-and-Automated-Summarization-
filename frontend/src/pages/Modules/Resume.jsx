import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";
import ResultCard from "../../components/Modules/ResultCard";

const Resume = () => {
  return (
    <ModuleLayout
      title="Resume Analyzer"
      description="Upload your resume to get ATS score and AI-powered suggestions."
    >
      <FileUploadBox />

      <button className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold hover:bg-blue-700 transition">
        Analyze Resume
      </button>

      <div className="mt-8">
        <ResultCard title="Analysis Results">
          <p className="text-gray-400">
            Upload a resume to begin analysis.
          </p>
        </ResultCard>
      </div>
    </ModuleLayout>
  );
};

export default Resume;