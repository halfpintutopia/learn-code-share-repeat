import React from 'react';
import { Link } from "react-router-dom";

import logo from '../../public/media/images/logo-dark.svg';

import "./sass/app.scss";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRightLong } from "@fortawesome/free-solid-svg-icons";

const Header = () => {

  return (
    <header className="primary-header container" data-width="wide">
      <section className="wrapper">
        <div className="primary-header__inner">
          <Link to="/">
            <span className="sr-only">Home</span>
            <img src={logo} alt="Logo for website" />
          </Link>
          <nav>
            <Link to="/join/register">
              <button
                className="green">
                Start
                <FontAwesomeIcon icon={faArrowRightLong} />
              </button>
            </Link>
          </nav>
        </div>
      </section>


    </header>
  );
};

export default Header;