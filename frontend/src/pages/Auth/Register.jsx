import { Link } from "react-router-dom";

import AuthLayout from "../../layouts/AuthLayout";
import AuthCard from "../../components/Authentication/AuthCard";
import AuthHeader from "../../components/Authentication/AuthHeader";
import AuthInput from "../../components/Authentication/AuthInput";
import PasswordInput from "../../components/Authentication/PasswordInput";
import Divider from "../../components/Authentication/Divider";
import SocialButtons from "../../components/Authentication/SocialButtons";

const Register = () => {
  return (
    <AuthLayout>
      <AuthCard>
        <AuthHeader
          title="Create Account 🚀"
          subtitle="Join SummarAI and start using AI-powered tools."
        />

        <AuthInput
          label="Full Name"
          placeholder="Enter your full name"
        />

        <AuthInput
          label="Email"
          type="email"
          placeholder="Enter your email"
        />

        <PasswordInput />

        <div className="mb-6">
          <label className="flex items-center gap-2 text-sm text-gray-400">
            <input type="checkbox" />
            I agree to the Terms & Conditions
          </label>
        </div>

        <button className="w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700">
          Create Account
        </button>

        <Divider />

        <SocialButtons />

        <p className="mt-8 text-center text-gray-400">
          Already have an account?{" "}
          <Link
            to="/login"
            className="font-medium text-blue-500 hover:text-blue-400"
          >
            Login
          </Link>
        </p>
      </AuthCard>
    </AuthLayout>
  );
};

export default Register;