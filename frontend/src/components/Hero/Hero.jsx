import { ArrowRight } from "lucide-react";

const Hero = () => {
  return (
    <section className="relative min-h-screen overflow-hidden bg-[#09090B] flex items-center justify-center px-6">

      {/* Background Glow */}
      <div className="absolute top-20 left-20 h-80 w-80 rounded-full bg-blue-600/20 blur-[120px]" />

      <div className="absolute bottom-10 right-10 h-80 w-80 rounded-full bg-violet-600/20 blur-[120px]" />

      {/* Hero Content */}
      <div className="relative z-10 max-w-5xl text-center">

        <p className="inline-block rounded-full border border-blue-500/30 bg-blue-500/10 px-5 py-2 text-blue-400 font-medium">
          🚀 AI Powered Multi Modal Platform
        </p>

        <h1 className="mt-8 text-6xl md:text-7xl font-extrabold text-white leading-tight">
          One Platform.
        </h1>

        <h2 className="mt-3 text-6xl md:text-7xl font-extrabold bg-gradient-to-r from-blue-400 via-cyan-300 to-violet-400 bg-clip-text text-transparent">
          Five AI Tools.
        </h2>

        <p className="mt-8 max-w-3xl mx-auto text-xl text-gray-400 leading-8">
          Analyze resumes, summarize PDFs, videos, audio recordings and text
          using one intelligent AI platform built for students, researchers,
          recruiters and professionals.
        </p>

        <div className="mt-12 flex flex-col sm:flex-row justify-center gap-5">

  <button className="flex items-center justify-center gap-2 rounded-xl bg-blue-600 px-8 py-4 font-semibold text-white hover:bg-blue-700 transition">

    Launch Platform

    <ArrowRight size={20} />

  </button>

  <button className="flex items-center justify-center gap-2 rounded-xl border border-gray-700 px-8 py-4 text-white hover:bg-gray-800 transition">


    View GitHub

  </button>

    </div>

      </div>

    </section>
  );
};

export default Hero;