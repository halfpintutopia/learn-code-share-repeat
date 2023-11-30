import React, {useState, useEffect, useRef} from 'react';

const Modal = ({isOpen, hasCloseBtn, onClose, children}) => {
  const [isModalOpen, setModalOpen] = useState(isOpen);
  const modalRef = useRef();

  useEffect(() => {
    setModalOpen(isOpen);
  }, [isOpen]);

  useEffect(() => {
    const modalElement = modalRef.current;
    if (modalElement) {
      if (isModalOpen) {
        modalElement.showModal();
      } else {
        modalElement.close();
      }
    }
    setModalOpen(isOpen);
  }, [isModalOpen]);

  const handleCloseModal = () => {
    if (onClose) {
      onClose();
    }
    setModalOpen(false);
  };

  const handleKeyDown = (event) => {
    if (event.key === "Escape") {
      handleCloseModal();
    }
  };

  return (
    <dialog ref={modalRef} onKeyDown={handleKeyDown} className="modal nav-dialog">
      {
        hasCloseBtn && (
          <button className="modal__close-btn" onClick={handleCloseModal}>Close</button>
        )
      }
      {children}
    </dialog>
  );
};

export default Modal;