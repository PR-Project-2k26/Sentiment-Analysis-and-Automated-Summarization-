const teamMembers = [
  {
    name: "Bhavya Vaish",
    role: "Lead Developer • Frontend, Backend & Video Module Integration",
  },
  {
    name: "Payal Choudhary",
    role: "Resume Analyzer Module",
  },
  {
    name: "Sparsh Shukla",
    role: "Text Summarizer Module",
  },
  {
    name: "Yash",
    role: "Audio Summarizer Module",
  },
  {
    name: "Sanidhya Digvijay Singh",
    role: "PDF Summarizer Module",
  },
];

const Team = () => {
  return (
    <section id="team" className="bg-[#0D0D0D] py-24 px-6">
      <div className="mx-auto max-w-7xl">

        <div className="text-center">
          <h2 className="text-5xl font-bold text-white">
            Meet Our Team
          </h2>

          <p className="mt-4 text-gray-400">
            The people behind this AI-powered platform.
          </p>
        </div>

        <div className="mt-16 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {teamMembers.map((member, index) => (
            <div
              key={index}
              className="rounded-2xl border border-white/10 bg-white/5 p-6 text-center transition hover:border-blue-500/40"
            >
              <div className="mx-auto flex h-24 w-24 items-center justify-center rounded-full bg-blue-600 text-3xl font-bold text-white">
                {member.name.charAt(0)}
              </div>

              <h3 className="mt-6 text-xl font-semibold text-white">
                {member.name}
              </h3>

              <p className="mt-2 text-gray-400">
                {member.role}
              </p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
};

export default Team;