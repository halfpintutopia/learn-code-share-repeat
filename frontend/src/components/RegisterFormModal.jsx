import React, {useEffect, useRef, useState} from 'react';
import Modal from "./Modal";

const initialRegisterFormModalData = {
  email: '',
  firstName: '',
  lastName: '',
  password: ''
};
const RegisterFormModal = ({onSubmit, isOpen, onClose}) => {
  const focusInputRef = useRef(null);
  const [formState, setFormState] = useState(initialRegisterFormModalData);

  useEffect(() => {
    if (isOpen && focusInputRef.current) {
      setTimeout(() => {
        if (focusInputRef.current !== null) {
          focusInputRef.current.focus();
        }
      }, 0);
    }
  }, [isOpen]);

  const handleInputChange = (event) => {
    const {name, value} = event.target;
    setFormState(prevFormData => ({
      ...prevFormData,
      [name]: value
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(formState);
    setFormState(initialRegisterFormModalData);
  };

  return (
    <Modal
      hasCloseBtn={true}
      isOpen={isOpen}
      onClose={onClose}
    >
      <form onSubmit={handleSubmit}>
        <div className="form-row">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            ref={focusInputRef}
            id="email"
            name="email"
            value={formState.email}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-row">
          <label htmlFor="firstName">First Name</label>
          <input
            type="text"
            ref={focusInputRef}
            id="firstName"
            name="firstName"
            value={formState.firstName}
            onChange={handleInputChange}
            required
          />
        </div>

        <div className="form-row">
          <label htmlFor="lastName">Last Name</label>
          <input
            type="text"
            ref={focusInputRef}
            id="lastName"
            name="lastName"
            value={formState.lastName}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-row">
          <button type="submit">Submit</button>
        </div>
      </form>
    </Modal>
  );
};

export default RegisterFormModal;