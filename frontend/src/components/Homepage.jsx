import React, { useContext } from "react";
import { AuthContext } from "./AuthContext";
import VideoListPage from "./VideoListPage";
import LandingPage from "./LandingPage";
import NavBar from "./NavBar";

const HomePage = () => {
  const { isAuthenticated } = useContext(AuthContext);
  return (
    <>
      <NavBar />
      {
        isAuthenticated ? (
          <VideoListPage />
        ) : (
          <LandingPage />
        )
      }
    </>
  );
};

export default HomePage;
