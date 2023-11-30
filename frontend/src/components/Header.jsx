import React, {useState} from 'react';
import {Link} from "react-router-dom";

import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faArrowRightLong} from '@fortawesome/free-solid-svg-icons';

import logo from '../../public/media/images/logo-dark.svg';

import RegisterFormModal from "./RegisterFormModal";

import "./sass/app.scss";

const Header = () => {

  const [isRegisterFormModalOpen, setRegisterFormModalOpen] = useState(false);
  const [registerFormData, setRegisterFormData] = useState(null);

  const handleOpenRegisterModal = () => {
    setRegisterFormModalOpen(true);
  };

  const handleCloseRegisterModal = () => {
    setRegisterFormModalOpen(false);
  };

  const handleFormSubmit = (data) => {
    setRegisterFormData(data);
    handleCloseRegisterModal();
  };

  return (
    <header className="primary-header container" data-width="wide">
      <section className="wrapper">
        <div className="primary-header__inner">
          <Link to="/">
            <span className="sr-only">Home</span>
            <img src={logo} alt="Logo for website"/>
          </Link>
          <nav>
            <div>
              <button
                onClick={handleOpenRegisterModal}
                className="green">
                Start
                <FontAwesomeIcon icon={faArrowRightLong}/>
              </button>
            </div>

            {
              registerFormData && registerFormData.email && (
                <div className="alert alert__success">
                  <b>{registerFormData.email}</b> has successfully signed up.
                </div>
              )
            }

            <RegisterFormModal
              isOpen={isRegisterFormModalOpen}
              onSubmit={handleFormSubmit}
              onClose={handleCloseRegisterModal}
            />
          </nav>
        </div>
      </section>


    </header>
  );
};

export default Header;