import React, {useContext} from "react";
import {AuthContext} from "./AuthContext";
import VideoListPage from "./VideoListPage";
import LandingPage from "./LandingPage";
import {Helmet} from "react-helmet-async";
import LogoDark from "../../public/media/images/logo-dark.svg";
import LogoLight from "../../public/media/images/logo-light.svg";
// import NavBar from "./NavBar";

const HomePage = () => {
  const {isAuthenticated} = useContext(AuthContext);
  return (
    <>
      <Helmet>
        <title>Home</title>
        <link
          rel="icon"
          type="type/svg+xml"
          href={LogoDark}
          media="(prefers-color-scheme:light)"
        />
        <link
          rel="icon"
          type="type/svg+xml"
          href={LogoLight}
          media="(prefers-color-scheme:dark)"
        />
      </Helmet>
      {
        isAuthenticated ? (
          <VideoListPage/>
        ) : (
          <LandingPage/>
        )
      }
    </>
  );
};

export default HomePage;
