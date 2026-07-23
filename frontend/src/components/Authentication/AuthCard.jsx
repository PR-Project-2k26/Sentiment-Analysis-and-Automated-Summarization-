const AuthCard = ({ children }) => {
  return (
    <div className="w-full max-w-md rounded-3xl border border-white/10 bg-white/5 p-10 backdrop-blur-xl shadow-2xl">
      {children}
    </div>
  );
};

export default AuthCard;