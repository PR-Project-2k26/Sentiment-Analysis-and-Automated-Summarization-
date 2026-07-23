const EmptyHistory = () => {
  return (
    <div className="rounded-xl border border-dashed border-zinc-700 p-16 text-center">
      <h2 className="text-2xl font-semibold text-white">
        No History Found
      </h2>

      <p className="mt-3 text-zinc-400">
        Start using Resume, PDF, Video, Audio or Text modules.
      </p>
    </div>
  );
};

export default EmptyHistory;