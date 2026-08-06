import { useState } from "react";
import ReactMarkdown from "react-markdown";

const formatMarkdown = (text = "") => {
  return text
    // Remove Markdown symbols if present
    .replace(/^##\s*/gm, "")
    .replace(/^###\s*/gm, "")
    .replace(/\*\*/g, "")

    // Convert known section titles into Markdown headings
    .replace(/^Overall Summary$/gim, "## Overall Summary\n")
    .replace(/^Strengths$/gim, "\n## Strengths\n")
    .replace(/^Weaknesses$/gim, "\n## Weaknesses\n")
    .replace(/^Missing Skills$/gim, "\n## Missing Skills\n")
    .replace(/^Recommendations$/gim, "\n## Recommendations\n")
    .replace(/^Career Roadmap$/gim, "\n## Career Roadmap\n")
    .replace(/^Conclusion$/gim, "\n## Conclusion\n");
};

const markdownComponents = {
  h2: ({ children }) => (
    <h2 className="mt-8 mb-5 text-3xl font-bold text-white">
      {children}
    </h2>
  ),

  p: ({ children }) => (
    <p className="mb-5 leading-8 text-gray-200">
      {children}
    </p>
  ),

  li: ({ children }) => (
    <li className="mb-2 text-gray-200">
      {children}
    </li>
  ),

  strong: ({ children }) => (
    <strong className="font-bold text-white">
      {children}
    </strong>
  ),
};

const tabs = [
  "ATS",
  "Job Match Breakdown",
  "Content",
  "AI Review",
  "Roadmap",
  "Suggestions",
];

const ResumeTabs = ({ result }) => {
  const [activeTab, setActiveTab] = useState("ATS");

  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">

      {/* Tabs */}
      <div className="mb-8 flex flex-wrap gap-3">
        {tabs.map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`rounded-xl px-5 py-2 transition ${
              activeTab === tab
                ? "bg-blue-500 text-white"
                : "bg-white/5 text-gray-300 hover:bg-white/10"
            }`}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* ATS */}
      {activeTab === "ATS" && (
        <div className="grid gap-8 md:grid-cols-2">

          <div>
            <h2 className="mb-4 text-2xl font-bold text-white">
              Strengths
            </h2>

            <ul className="space-y-3">
              {result.atsReport?.strengths?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </div>

          <div>
            <h2 className="mb-4 text-2xl font-bold text-white">
              Improvements
            </h2>

            <ul className="space-y-3">
              {result.atsReport?.improvements?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </div>

        </div>
      )}

      {/* Skills */}
      {activeTab === "Job Match Breakdown" && (
        <div className="grid gap-8 md:grid-cols-2">

          <div>
            <h2 className="mb-4 text-2xl font-bold text-white">
              Matched Skills
            </h2>

            <div className="flex flex-wrap gap-2">
              {result.matchedSkills?.map((skill) => (
                <span
                  key={skill}
                  className="rounded-full bg-green-600 px-3 py-1"
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>

          <div>
            <h2 className="mb-4 text-2xl font-bold text-white ">
              Missing Skills
            </h2>

            <div className="flex flex-wrap gap-2">
              {result.missingSkills?.map((skill) => (
                <span
                  key={skill}
                  className="rounded-full bg-red-600 px-3 py-1"
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>

        </div>
      )}

      {/* Content */}
      {activeTab === "Content" && (
        <div className="grid grid-cols-2 gap-4 md:grid-cols-4">

          {Object.entries(result.contentQuality || {})
            .filter(([key]) => key !== "Feedback" && key !== "Overall")
            .map(([key, value]) => (
              <div
                key={key}
                className={`rounded-xl p-5 transition-all duration-300 ${
                  value >= 8
                    ? "border border-green-500/30 bg-green-500/15"
                    : value >= 6
                    ? "border border-yellow-500/30 bg-yellow-500/15"
                    : "border border-red-500/30 bg-red-500/15"
                }`}
              >
                <p
                  className={`font-medium ${
                    value >= 8
                      ? "text-green-300"
                      : value >= 6
                      ? "text-yellow-300"
                      : "text-red-300"
                  }`}
                >
                  {key}
                </p>

                <h2
                  className={`mt-2 text-4xl font-extrabold ${
                    value >= 8
                      ? "text-green-400"
                      : value >= 6
                      ? "text-yellow-400"
                      : "text-red-400"
                  }`}
                >
                  {value}/10
                </h2>

              </div>
            ))}

        </div>
      )}

      {/* AI Review */}
      {activeTab === "AI Review" && (
        <div className="prose prose-invert max-w-none">
          <ReactMarkdown components={markdownComponents}>
            {formatMarkdown(result.aiReview)}
          </ReactMarkdown>
        </div>
      )}

      {/* Roadmap */}
      {activeTab === "Roadmap" && (
        <div className="prose prose-invert max-w-none">
          <ReactMarkdown components={markdownComponents}>
            {formatMarkdown(result.careerRoadmap)}
          </ReactMarkdown>
        </div>
      )}

      {/* Suggestions */}
      {activeTab === "Suggestions" && (
        <div className="space-y-8">

          {["High Priority", "Medium Priority", "Low Priority"].map(
            (level) =>
              result.suggestions?.[level]?.length > 0 && (
                <div key={level}>

                  <h2 className="mb-4 text-2xl font-bold">
                    {level}
                  </h2>

                  <ul className="list-disc space-y-2 pl-6">
                    {result.suggestions[level].map((item, index) => (
                      <li key={index}>
                      {item.replace(/\*\*/g, "")}
                      </li>
                    ))}
                  </ul>

                </div>
              )
          )}

        </div>
      )}

    </div>
  );
};

export default ResumeTabs;