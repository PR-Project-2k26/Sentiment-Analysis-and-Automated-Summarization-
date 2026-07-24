import { useState } from "react";

import ModuleLayout from "../../layouts/ModuleLayout";
import ResultCard from "../../components/Modules/ResultCard";

import { summarizeText } from "../../services/textService";

const Text = () => {
  const [text, setText] = useState("");
  const [length, setLength] = useState("Medium");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSummarize = async () => {
    if (!text.trim()) {
      alert("Please enter some text.");
      return;
    }

    try {
      setLoading(true);

      const response = await summarizeText(text, length);

      setResult(response);
    } catch (error) {
      console.error(error);

      alert(
        error?.response?.data?.message ||
          "Failed to summarize the text."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <ModuleLayout
      title="Text Summarizer"
      description="Paste text and generate an AI-powered summary with sentiment analysis."
    >
      {/* Length Selection */}
      <div className="mb-4">
        <label className="mb-2 block text-sm font-medium text-gray-300">
          Summary Length
        </label>

        <select
          value={length}
          onChange={(e) => setLength(e.target.value)}
          className="rounded-xl border border-white/10 bg-white/5 px-4 py-2 text-white outline-none focus:border-blue-500"
        >
          <option className="bg-gray-900">Short</option>
          <option className="bg-gray-900">Medium</option>
          <option className="bg-gray-900">Long</option>
        </select>
      </div>

      {/* Text Input */}
      <textarea
        rows={12}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste your text here..."
        className="w-full rounded-2xl border border-white/10 bg-white/5 p-5 text-white outline-none focus:border-blue-500"
      />

      {/* Button */}
      <button
        onClick={handleSummarize}
        disabled={loading}
        className="mt-6 rounded-xl bg-blue-600 px-6 py-3 font-semibold transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Summarizing..." : "Summarize Text"}
      </button>

      {/* Results */}
      <div className="mt-8 space-y-6">

        <ResultCard title="Summary">
          {result ? (
            <p className="whitespace-pre-wrap text-gray-300">
              {result.summary}
            </p>
          ) : (
            <p className="text-gray-400">
              Enter some text to generate a summary.
            </p>
          )}
        </ResultCard>

        {result && (
          <>
            <ResultCard title="Emotion">
              <p className="text-gray-300">{result.emotion}</p>
            </ResultCard>

            <ResultCard title="Key Topics">
              <ul className="list-disc space-y-2 pl-6 text-gray-300">
                {result.topics.map((topic, index) => (
                  <li key={index}>{topic}</li>
                ))}
              </ul>
            </ResultCard>

            <ResultCard title="Keywords">
              <div className="flex flex-wrap gap-2">
                {result.keywords.map((keyword, index) => (
                  <span
                    key={index}
                    className="rounded-full bg-blue-600/20 px-3 py-1 text-sm text-blue-300"
                  >
                    {keyword}
                  </span>
                ))}
              </div>
            </ResultCard>

            <ResultCard title="Readability">
              <p className="text-gray-300">
                {result.readability}
              </p>
            </ResultCard>

            <ResultCard title="Sentiment Analysis">
              <div className="grid grid-cols-2 gap-4 text-gray-300 md:grid-cols-4">
                <div>
                  <p className="text-sm text-gray-400">Positive</p>
                  <p>{result.sentiment.positive}%</p>
                </div>

                <div>
                  <p className="text-sm text-gray-400">Neutral</p>
                  <p>{result.sentiment.neutral}%</p>
                </div>

                <div>
                  <p className="text-sm text-gray-400">Negative</p>
                  <p>{result.sentiment.negative}%</p>
                </div>

                <div>
                  <p className="text-sm text-gray-400">Compound</p>
                  <p>{result.sentiment.compound}</p>
                </div>
              </div>
            </ResultCard>

            <ResultCard title="Statistics">
              <div className="grid grid-cols-2 gap-4 text-gray-300 md:grid-cols-3">
                <div>
                  <p className="text-sm text-gray-400">Original Words</p>
                  <p>{result.stats.original_words}</p>
                </div>

                <div>
                  <p className="text-sm text-gray-400">Summary Words</p>
                  <p>{result.stats.summary_words}</p>
                </div>

                <div>
                  <p className="text-sm text-gray-400">Compression</p>
                  <p>{result.stats.compression_pct}%</p>
                </div>

                <div>
                  <p className="text-sm text-gray-400">Original Read Time</p>
                  <p>{result.stats.reading_time_original_sec}s</p>
                </div>

                <div>
                  <p className="text-sm text-gray-400">Summary Read Time</p>
                  <p>{result.stats.reading_time_summary_sec}s</p>
                </div>

                <div>
                  <p className="text-sm text-gray-400">Latency</p>
                  <p>{result.latency_sec}s</p>
                </div>
              </div>
            </ResultCard>
          </>
        )}
      </div>
    </ModuleLayout>
  );
};

export default Text;