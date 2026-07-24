import { ArrowRight } from "lucide-react";
import { useNavigate } from "react-router-dom";

const Hero = () => {
  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  const handleGetStarted = () => {
    if (token) {
      navigate("/dashboard");
    } else {
      navigate("/login");
    }
  };

  const handleGitHub = () => {
    window.open(
      "https://github.com/PR-Project-2k26/Sentiment-Analysis-and-Automated-Summarization-",
      "_blank"
    );
  };

  return (
    <section className="relative flex min-h-screen items-center justify-center overflow-hidden bg-[#09090B] px-6 pt-20">

      {/* Background Glow */}
      <div className="absolute left-20 top-20 h-80 w-80 rounded-full bg-blue-600/20 blur-[120px]" />
      <div className="absolute bottom-10 right-10 h-80 w-80 rounded-full bg-violet-600/20 blur-[120px]" />

      {/* Hero Content */}
      <div className="relative z-10 max-w-5xl text-center">

        <p className="inline-block rounded-full border border-blue-500/30 bg-blue-500/10 px-5 py-2 font-medium text-blue-400">
          AI Powered Multi Modal Platform
        </p>

        <h1 className="mt-8 text-6xl font-extrabold leading-tight text-white md:text-7xl">
          One Platform.
        </h1>

        <h2 className="mt-3 bg-gradient-to-r from-blue-400 via-cyan-300 to-violet-400 bg-clip-text text-6xl font-extrabold text-transparent md:text-7xl">
          Five AI Tools.
        </h2>

        <p className="mx-auto mt-8 max-w-3xl text-xl leading-8 text-gray-400">
          Analyze resumes, summarize PDFs, videos, audio recordings and text
          using one intelligent AI platform built for students, researchers,
          recruiters and professionals.
        </p>

        <div className="mt-12 flex flex-col justify-center gap-5 sm:flex-row">

          <button
            onClick={handleGetStarted}
            className="flex items-center justify-center gap-2 rounded-xl bg-blue-600 px-8 py-4 font-semibold text-white transition hover:bg-blue-700"
          >
            {token ? "Go to Dashboard" : "Get Started"}
            <ArrowRight size={20} />
          </button>

          <button
            onClick={handleGitHub}
            className="flex items-center justify-center gap-2 rounded-xl border border-gray-700 px-8 py-4 text-white transition hover:bg-gray-800"
          >
            View GitHub
          </button>

        </div>

      </div>

    </section>
  );
};

export default Hero;