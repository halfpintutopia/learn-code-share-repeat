import React, { useEffect, useRef } from 'react';
import { faClose } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const Modal = ({ name, isOpen, hasCloseBtn, onClose, children }) => {
  const modalRef = useRef();

  useEffect(() => {
    const modalElement = modalRef.current;
    if (modalElement) {
      if (isOpen) {
        modalElement.showModal();
      } else {
        modalElement.close();
      }
    }
  }, [ isOpen ]);

  const handleCloseModal = () => {
    if (onClose) {
      onClose();
    }
  };

  const handleKeyDown = (event) => {
    if (event.key === "Escape") {
      handleCloseModal();
    }
  };

  return (
    <dialog ref={ modalRef } onKeyDown={ handleKeyDown } className={ `modal modal__${ name }` }>
      {
        hasCloseBtn && (
          <button className="modal__close-btn" onClick={ handleCloseModal }><FontAwesomeIcon icon={ faClose }/></button>
        )
      }
      { children }
    </dialog>
  );
};

export default Modal;