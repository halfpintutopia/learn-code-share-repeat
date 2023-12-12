import React from 'react';
import { Link } from "react-router-dom";

import logo from '../../public/media/images/logo-light.svg';

import "./sass/app.scss";

const HeaderSimple = () => {

  return (
    <header className="secondary-header container" data-width="wide">
      <section className="wrapper">
        <div className="secondary-header__inner">
          <Link to="/">
            <span className="sr-only">Home</span>
            <img src={logo} alt="Logo for website" />
          </Link>
        </div>
      </section>


    </header>
  );
};

export default HeaderSimple;