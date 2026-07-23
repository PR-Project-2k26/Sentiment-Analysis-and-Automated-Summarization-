import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "../pages/Home";
import Resume from "../pages/Resume";
import PDF from "../pages/PDF";
import Video from "../pages/Video";
import Audio from "../pages/Audio";
import Text from "../pages/Text";

const AppRoutes = () => {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />} />

        <Route path="/resume" element={<Resume />} />

        <Route path="/pdf" element={<PDF />} />

        <Route path="/video" element={<Video />} />

        <Route path="/audio" element={<Audio />} />

        <Route path="/text" element={<Text />} />

      </Routes>
    </BrowserRouter>
  );
};

export default AppRoutes;