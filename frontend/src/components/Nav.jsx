import React, {useEffect, useState, useRef} from 'react';
import css from "./css/Nav.module.css";

const Nav = () => {

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
    <div className={css.Nav}>
      <nav>
        <button onClick={showHideModal}>Open</button>
      </nav>

      <dialog ref={modalRef}>
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
  );
};

export default Nav;