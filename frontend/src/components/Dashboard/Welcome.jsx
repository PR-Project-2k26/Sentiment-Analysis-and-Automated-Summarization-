const Welcome = ({ user }) => {
  const firstName = user?.name?.split(" ")[0];

  return (
    <div className="mb-10">
      <h1 className="text-4xl font-bold text-white">
        Welcome Back{firstName ? `, ${firstName}` : ""}
      </h1>

      <p className="mt-3 text-lg text-gray-400">
        Manage all your AI-powered summarization tools from one dashboard.
      </p>
    </div>
  );
};

export default Welcome;