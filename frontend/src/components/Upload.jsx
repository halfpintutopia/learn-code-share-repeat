import React, {useContext} from "react";
import {AuthContext} from "./AuthContext";
import NavBar from "./NavBar";
import Footer from "./Footer";
import JoinPage from "./JoinPage";
import UploadPage from "./UploadPage";

const Upload = () => {
  const {isAuthenticated} = useContext(AuthContext);
  return (
    <>
      <NavBar/>
      {
        isAuthenticated ? (
          <UploadPage/>
        ) : (
          <JoinPage/>
        )
      }
      <Footer/>
    </>
  );
};

export default Upload;
