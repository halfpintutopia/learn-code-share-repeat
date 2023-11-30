import {Link} from "react-router-dom";
import React, {useEffect, useState, useRef} from 'react';
import logo from '../../public/media/images/logo-dark.svg';
import "./sass/app.scss";

const Header = () => {
  const [modal, setModal] = useState(false);
  const modalRef = useRef();
  const showHideModal = () => {
    setModal(!modal);
  };

  const handleClickOutside = (event) => {
    if (event.target === modalRef.current) {
      setModal(false);
    }
  };

  useEffect(() => {
    if (modal) {
      modalRef.current.showModal();
      document.body.addEventListener('mousedown', handleClickOutside);
    } else {
      modalRef.current.close();
      document.body.removeEventListener('mousedown', handleClickOutside);
    }
    return () => {
      document.body.removeEventListener('mousedown', handleClickOutside);
    };
  }, [modal]);

  return (
    <header className="primary-header container" data-width="wide">
      <div className="wrapper">
        <div className="primary-header__inner">
          <Link to="/">
            <span className="sr-only">Home</span>
            <img src={logo} alt="Logo for website"/>
          </Link>
          <nav>
            <button onClick={showHideModal}>Open</button>
          </nav>

          <dialog ref={modalRef} className="nav-dialog">
            <form method="dialog">
              <label htmlFor="firstName">First Name</label>
              <input id="firstName" name="firstName" type="text"/>
              <button formMethod="dialog">cancel</button>
              <button>Submit</button>
            </form>
            <div>This is not a dialog but a modal</div>
            <button onClick={() => setModal(false)}>Close</button>
          </dialog>
        </div>
      </div>
    </header>
  );
};

export default Header;