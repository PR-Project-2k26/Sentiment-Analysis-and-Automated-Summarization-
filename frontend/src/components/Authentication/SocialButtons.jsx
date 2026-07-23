const SocialButtons = () => {
  return (
    <div className="space-y-3">

      <button
        className="w-full rounded-xl border border-white/10 bg-white/5 py-3 text-white transition hover:bg-white/10"
      >
        Continue with Google
      </button>

      <button
        className="w-full rounded-xl border border-white/10 bg-white/5 py-3 text-white transition hover:bg-white/10"
      >
        Continue with GitHub
      </button>

    </div>
  );
};

export default SocialButtons;