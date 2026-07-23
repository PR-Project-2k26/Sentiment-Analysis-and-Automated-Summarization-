const Dashboard = () => {
  return (
    <section className="bg-[#0D0D0D] py-24 px-6">
      <div className="max-w-7xl mx-auto">

        <div className="text-center">
          <h2 className="text-5xl font-bold text-white">
            Unified AI Dashboard
          </h2>

          <p className="mt-4 text-gray-400 max-w-3xl mx-auto">
            Access all AI tools from one modern dashboard with a clean,
            responsive interface.
          </p>
        </div>

        <div className="mt-16 rounded-3xl border border-white/10 bg-white/5 backdrop-blur-lg p-8 shadow-2xl">

          <div className="grid lg:grid-cols-4 gap-6">

            {/* Sidebar */}
            <div className="rounded-2xl bg-[#111] p-6">
              <h3 className="text-white font-bold text-xl">
                Dashboard
              </h3>

              <ul className="mt-6 space-y-4 text-gray-400">
                <li>📄 Resume Analyzer</li>
                <li>📕 PDF Summarizer</li>
                <li>🎥 Video Summarizer</li>
                <li>🎙 Audio Summarizer</li>
                <li>📝 Text Summarizer</li>
              </ul>
            </div>

            {/* Main Preview */}
            <div className="lg:col-span-3 rounded-2xl bg-[#151515] p-8">

              <div className="grid md:grid-cols-3 gap-6">

                <div className="rounded-xl bg-blue-600 p-6">
                  <p className="text-white text-sm">
                    Active Modules
                  </p>

                  <h2 className="mt-3 text-4xl font-bold text-white">
                    5
                  </h2>
                </div>

                <div className="rounded-xl bg-violet-600 p-6">
                  <p className="text-white text-sm">
                    Files Processed
                  </p>

                  <h2 className="mt-3 text-4xl font-bold text-white">
                    12K+
                  </h2>
                </div>

                <div className="rounded-xl bg-green-600 p-6">
                  <p className="text-white text-sm">
                    Accuracy
                  </p>

                  <h2 className="mt-3 text-4xl font-bold text-white">
                    98%
                  </h2>
                </div>

              </div>

              <div className="mt-8 h-64 rounded-xl border border-dashed border-gray-600 flex items-center justify-center text-gray-500">
                Dashboard Preview
              </div>

            </div>

          </div>

        </div>

      </div>
    </section>
  );
};

export default Dashboard;