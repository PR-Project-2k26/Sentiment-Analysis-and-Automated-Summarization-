import Navbar from "../components/Navbar/Navbar";
import Hero from "../components/Hero/Hero";
import Modules from "../components/Modules/Modules";
import Dashboard from "../components/Dashboard/Dashboard";
import Architecture from "../components/Architecture/Architecture";
import Team from "../components/Team/Team";
import Footer from "../components/Footer/Footer";

const Home = () => {
  return (
    <>
    <Navbar />
    <Hero />
    <Modules />
    <Dashboard />
    <Architecture />
    <Team />
    <Footer />
  </>
  );
};

export default Home;