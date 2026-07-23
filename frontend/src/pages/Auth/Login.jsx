import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthHeader from "../../components/Authentication/AuthHeader";
import AuthInput from "../../components/Authentication/AuthInput";
import PasswordInput from "../../components/Authentication/PasswordInput";

const Login = () => {
  return (
    <AuthLayout>
      <AuthCard>
        <AuthHeader
        title="Welcome Back 👋"
        subtitle="Sign in to continue using SummarAI."
        />

        <AuthInput
        label="Email"
        type="email"
        placeholder="Enter your email"
        />

        <PasswordInput />

        <div className="mb-6 flex items-center justify-between">

        <label className="flex items-center gap-2 text-sm text-gray-400">
            <input type="checkbox" />
            Remember Me
        </label>

        <button className="text-sm text-blue-400 hover:text-blue-300">
            Forgot Password?
        </button>

        </div>

        <button className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700">
        Login
        </button>
            </AuthCard>
            </AuthLayout>
  );
};

export default Login;