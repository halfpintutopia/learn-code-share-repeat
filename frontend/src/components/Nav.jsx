import React from 'react';
import {Link} from "react-router-dom";

const Nav = () => {
  return (
    <nav>
      <Link href="/watch">Watch</Link>
      <Link href="/my-work">My Work</Link>
    </nav>
  );
};

export default Nav;