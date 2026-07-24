const AuthCard = ({ children }) => {
  return (
    <div className="w-full max-w-[420px] border border-white/10 bg-[#111113]/90 p-8 shadow-[0_0_60px_rgba(0,0,0,0.35)] backdrop-blur-2xl">
      {children}
    </div>
  );
};

export default AuthCard;