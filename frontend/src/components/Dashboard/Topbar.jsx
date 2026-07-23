const Topbar = () => {
  return (
    <div className="flex items-center justify-between border-b border-white/10 pb-5">
      <input
        placeholder="Search modules..."
        className="w-96 rounded-xl border border-white/10 bg-white/5 px-4 py-3 text-white outline-none"
      />

      <div className="flex items-center gap-4">
        <button className="rounded-full bg-blue-600 px-4 py-2 text-white">
          Profile
        </button>
      </div>
    </div>
  );
};

export default Topbar;