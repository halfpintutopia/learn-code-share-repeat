import React from "react";
import Sidebar from "./Sidebar";
import Content from "./Content";
import NavBarSimple from "./NavBarSimple";

const HomePage = () => {
  return (
    <>
      <NavBarSimple />
      <Sidebar />
      <Content />
      {/* Add more components here if needed */}
    </>
  );
};

export default HomePage;
