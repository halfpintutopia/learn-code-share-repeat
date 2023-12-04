import Modal from "./Modal";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import AccessibleTabs from "./AccessibleTabs";
import React, { useEffect, useRef, useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRightLong } from "@fortawesome/free-solid-svg-icons";
import { useLocation } from "react-router-dom";
import queryString from 'query-string';


const RegisterLoginModal = () => {
  const location = useLocation();
  const { modal } = queryString.parse(location.search?.modal);
  const [isOpen, setIsOpen] = useState(!!modal);
  const focusInputRef = useRef(null);

  const handleOpenModal = () => {
    setIsOpen(true);
  };

  const handleCloseModal = () => {
    setIsOpen(false);
  };

  const tabs = [
    {
      id: 'login',
      title: 'Login',
      content: <LoginForm/>
    },
    {
      id: 'register',
      title: 'Register',
      content: <RegisterForm/>
    }
  ];

  useEffect(() => {
    if (isOpen && focusInputRef.current) {
      setTimeout(() => {
        if (focusInputRef.current !== null) {
          focusInputRef.current.focus();
        }
      }, 0);
    }
  }, [isOpen]);

  useEffect(() => {
    setIsOpen(!!modal);
  }, [modal]);


  return (
    <>
      <button
        onClick={handleOpenModal}
        className="green">
        Start
        <FontAwesomeIcon icon={faArrowRightLong}/>
      </button>
      <Modal
        name="register"
        hasCloseBtn={true}
        isOpen={isOpen}
        onClose={handleCloseModal}
      >
        <AccessibleTabs tabs={tabs}/>
      </Modal>
    </>
  );
};

export default RegisterLoginModal;