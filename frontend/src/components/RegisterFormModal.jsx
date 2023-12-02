import React, {useEffect, useRef, useState} from 'react';
import Modal from "./Modal";

const initialRegisterFormModalData = {
  username: '',
  email: '',
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

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formState)
      });
      if (!response.ok) {
        console.log(response);
        throw new Error('Network response was not OK');
      }
      console.log('response', response);

    } catch (error) {
      // TODO
    }


    onSubmit(formState);
    setFormState(initialRegisterFormModalData);
  };

  return (
    <Modal
      name="register"
      hasCloseBtn={true}
      isOpen={isOpen}
      onClose={onClose}
    >
      <h1>Join the LCSR Community</h1>
      <p>Have an account already? <b>Sign in</b></p>
      <form onSubmit={handleSubmit}>
        <div className="form-row">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            ref={focusInputRef}
            id="username"
            name="username"
            value={formState.username}
            onChange={handleInputChange}
            required
          />
        </div>

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
          <label htmlFor="password">Password</label>
          <input
            type="password"
            ref={focusInputRef}
            id="password"
            name="password"
            value={formState.password}
            onChange={handleInputChange}
            required
          />
        </div>
        <div className="form-row">
          <button className="btn btn__register" type="submit">Get Started</button>
        </div>
      </form>
    </Modal>
  );
};

export default RegisterFormModal;