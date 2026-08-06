import { useState } from "react";

import ModuleLayout from "../../layouts/ModuleLayout";
import FileUploadBox from "../../components/Modules/FileUploadBox";

import HeroScore from "../../components/Resume/HeroScore";
import ResumeTabs from "../../components/Resume/ResumeTabs";

import { analyzeResume } from "../../services/resumeService";
import { saveHistory } from "../../services/historyService";

const Resume = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    if (!selectedFile) {
      alert("Please select a Resume.");
      return;
    }

    try {
      setLoading(true);

      const response = await analyzeResume(
        selectedFile,
        jobDescription
      );

      setResult(response);

      await saveHistory({
        module: "Resume Analyzer",
        file_name: selectedFile.name,
        summary: JSON.stringify({
          resumeScore: response.resumeScore,
          atsScore: response.atsScore,
          skillScore: response.jobMatch?.score,
        }),
        processing_time: 0,
        status: "Completed",
      });
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
      title="AI Resume Analyzer"
      description="Upload your resume and compare it with any Job Description using AI."
    >
      <FileUploadBox
        selectedFile={selectedFile}
        onFileSelect={setSelectedFile}
        accept=".pdf"
        title="Upload Resume (PDF)"
      />

      <textarea
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        placeholder="Paste Job Description"
        className="mt-6 h-44 w-full rounded-2xl border border-white/10 bg-white/5 p-5 text-white"
      />

      <button
    onClick={handleAnalyze}
    disabled={loading}
    className="mt-6 rounded-2xl bg-blue-600 px-8 py-4 text-xl font-bold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
    >
    {loading ? "Analyzing Resume..." : "Analyze Resume"}
    </button>

      {result && (
        <div className="mt-10 space-y-8">
          {/* Hero Score */}
          <HeroScore
            score={result.resumeScore}
            ats={result.atsScore}
            job={result.jobMatch?.score}
            content={result.scoreBreakdown?.["Content Quality"]}
            structure={result.scoreBreakdown?.["Resume Structure"]}
          />

          {/* Score Breakdown */}
          <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
            <h2 className="mb-6 text-center text-2xl font-bold text-white">
            Score Breakdown
            </h2>

            {Object.entries(result.scoreBreakdown || {}).map(
              ([title, score]) => {
                const total =
                  title === "Job Match" ? 40 : 20;

                return (
                  <div
                    key={title}
                    className="mb-5"
                  >
                    <div className="mb-2 flex justify-between">
                      <span className="font-medium">
                        {title}
                      </span>

                      <span>
                        {score}/{total}
                      </span>
                    </div>

                    <div className="h-2 rounded-full bg-gray-800">
                      <div
                        className="h-2 rounded-full bg-blue-500"
                        style={{
                          width: `${Math.min(
                            (score / total) * 100,
                            100
                          )}%`,
                        }}
                      />
                    </div>
                  </div>
                );
              }
            )}
          </div>

          {/* Tabs */}
          <ResumeTabs result={result} />
        </div>
      )}
    </ModuleLayout>
  );
};

export default Resume;