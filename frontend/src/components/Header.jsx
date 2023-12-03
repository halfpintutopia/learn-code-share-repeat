import React from 'react';
import {Link} from "react-router-dom";

import logo from '../../public/media/images/logo-dark.svg';

import "./sass/app.scss";
import RegisterLoginModal from "./RegisterLoginModal";

const Header = () => {

  return (
    <header className="primary-header container" data-width="wide">
      <section className="wrapper">
        <div className="primary-header__inner">
          <Link to="/">
            <span className="sr-only">Home</span>
            <img src={logo} alt="Logo for website"/>
          </Link>
          <nav>
            <RegisterLoginModal />
          </nav>
        </div>
      </section>


    </header>
  );
};

export default Header;