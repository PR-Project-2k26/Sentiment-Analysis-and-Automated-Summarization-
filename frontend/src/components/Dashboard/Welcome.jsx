const Welcome = ({ user }) => {
  return (
    <div className="mb-10">
      <h1 className="text-4xl font-bold text-white">
        👋 Welcome Back{user?.name ? `, ${user.name}` : ""}
      </h1>

      <p className="mt-3 text-lg text-gray-400">
        Manage all your AI-powered summarization tools from one dashboard.
      </p>
    </div>
  );
};

export default Welcome;