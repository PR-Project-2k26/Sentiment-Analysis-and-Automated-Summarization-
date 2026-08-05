import { useState } from "react";

const tabs = [
  "ATS",
  "Skills",
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
                ? "bg-red-500 text-white"
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

            <h2 className="mb-4 text-2xl font-bold text-green-400">
              Strengths
            </h2>

            <ul className="space-y-3">

              {result.atsReport?.strengths?.map((item, index) => (

                <li key={index}>✅ {item}</li>

              ))}

            </ul>

          </div>

          <div>

            <h2 className="mb-4 text-2xl font-bold text-yellow-400">
              Improvements
            </h2>

            <ul className="space-y-3">

              {result.atsReport?.improvements?.map((item, index) => (

                <li key={index}>⚠️ {item}</li>

              ))}

            </ul>

          </div>

        </div>

      )}

      {/* Skills */}

      {activeTab === "Skills" && (

        <div className="grid gap-8 md:grid-cols-2">

          <div>

            <h2 className="mb-4 text-2xl font-bold text-green-400">
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

            <h2 className="mb-4 text-2xl font-bold text-red-400">
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
                className="rounded-xl bg-white/5 p-5"
              >

                <p className="text-gray-400">{key}</p>

                <h2 className="mt-2 text-3xl font-bold">
                  {value}/10
                </h2>

              </div>

            ))}

        </div>

      )}

      {/* AI Review */}

      {activeTab === "AI Review" && (

        <div className="whitespace-pre-wrap leading-8">

          {result.aiReview}

        </div>

      )}

      {/* Roadmap */}

      {activeTab === "Roadmap" && (

        <div className="whitespace-pre-wrap leading-8">

          {result.careerRoadmap}

        </div>

      )}

      {/* Suggestions */}

      {activeTab === "Suggestions" && (

        <div className="space-y-8">

          {["High Priority", "Medium Priority", "Low Priority"].map((level) => (

            result.suggestions?.[level]?.length > 0 && (

              <div key={level}>

                <h2 className="mb-4 text-2xl font-bold">

                  {level}

                </h2>

                <ul className="list-disc space-y-2 pl-6">

                  {result.suggestions[level].map((item, index) => (

                    <li key={index}>{item}</li>

                  ))}

                </ul>

              </div>

            )

          ))}

        </div>

      )}

    </div>
  );
};

export default ResumeTabs;