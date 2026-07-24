import { useState } from "react";
import { Eye, EyeOff } from "lucide-react";

const PasswordInput = ({
  name,
  value,
  onChange,
  placeholder = "Enter your password",
  label = "Password",
}) => {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div>
      <label className="mb-2 block text-sm font-medium text-gray-300">
        {label}
      </label>

      <div className="relative">

        <input
          type={showPassword ? "text" : "password"}
          name={name}
          value={value}
          onChange={onChange}
          placeholder={placeholder}
          autoComplete="current-password"
          className="
            w-full
            rounded-xl
            border
            border-white/10
            bg-[#18181B]
            px-4
            py-3
            pr-12
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

        <button
          type="button"
          onClick={() => setShowPassword((prev) => !prev)}
          className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-500 transition hover:text-white"
        >
          {showPassword ? (
            <EyeOff size={18} />
          ) : (
            <Eye size={18} />
          )}
        </button>

      </div>
    </div>
  );
};

export default PasswordInput;