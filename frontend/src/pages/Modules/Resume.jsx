import { useState } from "react";

import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";
import ResultCard from "../../components/Modules/ResultCard";

import { analyzeResume } from "../../services/resumeService";

const Resume = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    if (!selectedFile) {
      alert("Please select a resume.");
      return;
    }

    try {
      setLoading(true);

      const response = await analyzeResume(
        selectedFile,
        jobDescription
      );

      setResult(response);

    } catch (error) {
      console.error(error);

      alert(
        error.response?.data?.message ||
        "Failed to analyze resume."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <ModuleLayout
      title="Resume Analyzer"
      description="Upload your resume to get ATS score and AI-powered suggestions."
    >
      <FileUploadBox
        selectedFile={selectedFile}
        onFileSelect={setSelectedFile}
      />

      <textarea
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        placeholder="Paste Job Description (Optional)"
        className="mt-6 h-40 w-full rounded-xl border border-white/10 bg-white/5 p-4 text-white outline-none"
      />

      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {result && (
        <div className="mt-8 space-y-6">

          <ResultCard title="Resume Scores">
            <div className="grid grid-cols-1 gap-4 md:grid-cols-3">

              <div className="rounded-xl bg-white/5 p-4">
                <p className="text-gray-400">Resume Score</p>
                <h2 className="text-3xl font-bold text-green-400">
                  {result.resumeScore}/100
                </h2>
              </div>

              <div className="rounded-xl bg-white/5 p-4">
                <p className="text-gray-400">ATS Score</p>
                <h2 className="text-3xl font-bold text-blue-400">
                  {result.atsScore}/20
                </h2>
              </div>

              <div className="rounded-xl bg-white/5 p-4">
                <p className="text-gray-400">Skill Match</p>
                <h2 className="text-3xl font-bold text-purple-400">
                  {result.skillScore}/40
                </h2>
              </div>

            </div>
          </ResultCard>

          <ResultCard title="Matched Skills">
            <div className="flex flex-wrap gap-2">
              {result.matchedSkills.map((skill) => (
                <span
                  key={skill}
                  className="rounded-full bg-green-600 px-3 py-1 text-sm"
                >
                  {skill}
                </span>
              ))}
            </div>
          </ResultCard>

          <ResultCard title="Missing Skills">
            <div className="flex flex-wrap gap-2">
              {result.missingSkills.map((skill) => (
                <span
                  key={skill}
                  className="rounded-full bg-red-600 px-3 py-1 text-sm"
                >
                  {skill}
                </span>
              ))}
            </div>
          </ResultCard>

          <ResultCard title="Suggestions">
            <ul className="list-disc space-y-2 pl-6">
              {result.suggestions.map((item, index) => (
                <li key={index}>
                  {item}
                </li>
              ))}
            </ul>
          </ResultCard>

        </div>
      )}
    </ModuleLayout>
  );
};

export default Resume;