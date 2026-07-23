import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthHeader from "../../components/Authentication/AuthHeader";
import AuthInput from "../../components/Authentication/AuthInput";
import PasswordInput from "../../components/Authentication/PasswordInput";
import Divider from "../../components/Authentication/Divider";
import SocialButtons from "../../components/Authentication/SocialButtons";
import AuthFooter from "../../components/Authentication/AuthFooter";
import { Link } from "react-router-dom";

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

          <Link
            to="/forgot-password"
            className="text-sm text-blue-400 hover:text-blue-300"
            >
            Forgot Password?
            </Link>
        </div>

        <button className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700">
          Login
        </button>

        {/* Divider */}
        <Divider />

        {/* Social Login Buttons */}
        <SocialButtons />

        {/* Register Link */}
        <AuthFooter />
      </AuthCard>
    </AuthLayout>
  );
};

export default Login;