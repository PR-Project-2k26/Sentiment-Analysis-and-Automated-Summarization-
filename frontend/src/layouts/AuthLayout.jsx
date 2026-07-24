import { CheckCircle2 } from "lucide-react";

const features = [
  "Resume Analysis",
  "PDF Summarization",
  "Video & Audio Summarization",
  "Text Summarization",
];

const AuthLayout = ({ children }) => {
  return (
    <div className="relative flex h-screen overflow-hidden bg-[#09090B]">

      {/* Background */}
      <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:48px_48px]" />

      <div className="absolute -left-40 top-0 h-[500px] w-[500px] rounded-full bg-blue-600/10 blur-[170px]" />
      <div className="absolute -right-40 bottom-0 h-[500px] w-[500px] rounded-full bg-violet-600/10 blur-[170px]" />

      <div className="relative z-10 mx-auto flex w-full max-w-7xl items-center justify-between px-10">

        {/* Left */}
        <div className="hidden max-w-xl lg:block">

          <h1 className="text-6xl font-black tracking-tight text-white">
            Summar
            <span className="text-blue-500">AI</span>
          </h1>

          <p className="mt-8 text-xl leading-9 text-gray-400">
            One intelligent platform to analyze resumes and summarize
            PDFs, videos, audio recordings, and text using AI.
          </p>

          <div className="mt-12 space-y-5">

            {features.map((feature) => (
              <div
                key={feature}
                className="flex items-center gap-4 text-lg text-gray-300"
              >
                <CheckCircle2
                  size={22}
                  className="text-blue-500"
                />
                {feature}
              </div>
            ))}

          </div>

        </div>

        {/* Right */}
        <div className="flex w-full justify-center lg:w-auto">
          {children}
        </div>

      </div>

    </div>
  );
};

export default AuthLayout;