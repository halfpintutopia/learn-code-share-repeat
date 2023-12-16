import React, { useContext } from "react";
import { AuthContext } from "./AuthContext";
import VideoListPage from "./VideoListPage";
import LandingPage from "./LandingPage";

const HomePage = () => {
  const { isAuthenticated } = useContext(AuthContext);
  return isAuthenticated ? <VideoListPage /> : <LandingPage />;
};

export default HomePage;
