const AuthInput = ({
  label,
  type = "text",
  placeholder,
  name,
  value,
  onChange,
}) => {
  return (
    <div>
      <label className="mb-2 block text-sm font-medium text-gray-300">
        {label}
      </label>

      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        autoComplete="off"
        className="
          w-full
          rounded-xl
          border
          border-white/10
          bg-[#18181B]
          px-4
          py-3
          text-white
          placeholder:text-gray-500
          outline-none
          transition-all
          duration-200
          focus:border-blue-500
          focus:bg-[#1E1E22]
          focus:ring-2
          focus:ring-blue-500/20
        "
      />
    </div>
  );
};

export default AuthInput;