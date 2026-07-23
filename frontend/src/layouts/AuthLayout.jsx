const AuthLayout = ({ children }) => {
  return (
    <div className="relative min-h-screen overflow-hidden bg-[#09090B]">

      {/* Background Glow */}
      <div className="absolute -top-40 -left-40 h-96 w-96 rounded-full bg-blue-600/20 blur-[140px]" />
      <div className="absolute bottom-0 right-0 h-96 w-96 rounded-full bg-violet-600/20 blur-[140px]" />

      {/* Grid */}
      <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:40px_40px]" />

      <div className="relative z-10 mx-auto flex min-h-screen max-w-7xl items-center justify-between px-6">

        {/* Left Side */}
        <div className="hidden lg:block max-w-xl">

          <h1 className="text-6xl font-extrabold text-white">
            Summar<span className="text-blue-500">AI</span>
          </h1>

          <p className="mt-6 text-xl text-gray-400 leading-9">
            One intelligent platform for resume analysis,
            PDF summarization, video summarization,
            audio transcription and text summarization.
          </p>

          <div className="mt-10 space-y-5">

            <Feature text="ATS Resume Analysis" />
            <Feature text="PDF Summarization" />
            <Feature text="Video Summarization" />
            <Feature text="Audio Summarization" />
            <Feature text="Text Summarization" />

          </div>

        </div>

        {/* Right Side */}
        <div className="w-full lg:w-auto">
          {children}
        </div>

      </div>

    </div>
  );
};

const Feature = ({ text }) => (
  <div className="flex items-center gap-3 text-gray-300">
    <div className="h-2 w-2 rounded-full bg-blue-500" />
    {text}
  </div>
);

export default AuthLayout;