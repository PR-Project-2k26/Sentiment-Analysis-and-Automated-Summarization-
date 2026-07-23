const AuthInput = ({
  label,
  type = "text",
  placeholder,
}) => {
  return (
    <div className="mb-5">
      <label className="mb-2 block text-sm font-medium text-gray-300">
        {label}
      </label>

      <input
        type={type}
        placeholder={placeholder}
        className="w-full rounded-xl border border-white/10 bg-white/5 px-4 py-3 text-white outline-none transition-all placeholder:text-gray-500 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20"
      />
    </div>
  );
};

export default AuthInput;