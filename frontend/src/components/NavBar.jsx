import { useContext, useState } from 'react';
import { Link, useNavigate } from "react-router-dom";

import "./sass/main.scss";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRightLong, faArrowUpFromBracket } from "@fortawesome/free-solid-svg-icons";
import { AuthContext } from "./AuthContext";
import Logo from "./assets/Logo";

const NavBar = () => {
  const { isAuthenticated, logout } = useContext(AuthContext);
  const [ navVisible, setNavVisible ] = useState(false);
  const navigate = useNavigate();

  const toggleNav = () => {
    setNavVisible(!navVisible);
  };

  const handleLogOut = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    logout();
    navigate('/');
  };

  return (
    <>
      <header className="primary-header container" data-width="wide">
        <div className="logo">
          <Link to="/">
            <span className="sr-only">Home</span>
            <Logo/>
          </Link>
        </div>
        {
          isAuthenticated ? (
            <>
              <button
                className="nav-toggle"
                aria-controls="primary-navigation"
                aria-expanded={ navVisible }
                onClick={ toggleNav }
              >
                <svg width="34" height="18" viewBox="0 0 34 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M1 1H33" stroke="#0D0D0D" strokeWidth="2" strokeLinecap="round"/>
                  <path d="M7 9H27" stroke="#0D0D0D" strokeWidth="2" strokeLinecap="round"/>
                  <path d="M1 17H33" stroke="#0D0D0D" strokeWidth="2" strokeLinecap="round"/>
                </svg>
                <span className="sr-only">Menu</span>
              </button>
            </>
          ) : (
            <Link to="/join/register" className="align-right">
              <button
                className="btn green">
                Start
                <FontAwesomeIcon icon={ faArrowRightLong }/>
              </button>
            </Link>
          )
        }
        <nav>
          <ul id="primary-navigation" data-visible={ navVisible } className="primary-navigation">
            {
              isAuthenticated && (
                <>
                  {/*<SearchBar />*/ }
                  <li>
                    <Link to="/watch">
                      Watch
                    </Link>
                  </li>
                  <li>
                    <Link to="/me">
                      My Work
                    </Link>
                  </li>
                  <li>
                    <Link to="/upload">
                      <button
                        className="btn green">
                        Upload
                        <FontAwesomeIcon icon={ faArrowUpFromBracket }/>
                      </button>
                    </Link>
                  </li>
                  <li>
                    <button className="btn green" onClick={handleLogOut}>Logout</button>
                  </li>
                </>
              )
            }
          </ul>
        </nav>
      </header>
    </>
  );
};

export default NavBar;