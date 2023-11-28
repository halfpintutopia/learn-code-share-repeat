import React from 'react';
import {Link} from "react-router-dom";
import Nav from "./Nav";

const Header = () => {
  return (
    <header>
      <div className="bar">
        <Link href="/">Logo</Link>
      </div>
      <Nav/>
    </header>
  );
};

export default Header;