import React, {useContext} from "react";
import {AuthContext} from "./AuthContext";
import VideoListPage from "./VideoListPage";
import LandingPage from "./LandingPage";
import NavBar from "./NavBar";
import Footer from "./Footer";

const HomePage = () => {
  const {isAuthenticated} = useContext(AuthContext);
  // console.log('authenticated', isAuthenticated);
  return (
    <>
      <NavBar/>
      {
        isAuthenticated ? (
          <VideoListPage/>
        ) : (
          <LandingPage/>
        )
      }
      <Footer/>
    </>
  );
};

export default HomePage;
