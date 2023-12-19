import React, { useContext, useRef, useState } from 'react';
import { Link } from "react-router-dom";
import { postData } from "./fetchData";
import { AuthContext } from "./AuthContext";

const initialRegisterFormModalData = {
  username: '',
  password: ''
};

const initialErrorState = {
  username: '',
  password: ''
};

const api = `http://localhost:8000/auth/token/`;

const LoginForm = () => {
  const { setIsAuthenticated } = useContext(AuthContext);
  const focusInputRef = useRef(null);
  const [formState, setFormState] = useState(initialRegisterFormModalData);
  const [errors, setErrors] = useState(initialErrorState);
  const [errorMessage, setErrorMessage] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const validateForm = () => {
    let newErrors = { ...initialErrorState };
    let formIsValid = true;

    if (!formState.username) {
      formIsValid = false;
      newErrors.username = 'Username is required';
    }

    if (!formState.password) {
      formIsValid = false;
      newErrors.password = 'Password is required';
    }

    setErrors(newErrors);
    return formIsValid;
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormState(prevFormData => ({
      ...prevFormData,
      [name]: value
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (validateForm()) {
      try {
        const response = await postData(api, formState);

        if (!response.ok) {
          const errorData = await response.json();
          setErrorMessage(errorData.detail);
        } else {
          const data = await response.json();
          localStorage.setItem('accessToken', data.access);
          localStorage.setItem('refreshToken', data.refresh);
          setIsAuthenticated(true);
          setSuccessMessage('You have successfully created an account, please ');
          setFormState(initialRegisterFormModalData);
        }

      } catch (error) {
        console.error(error);
        setErrorMessage(('An unexpected error occurred.'));
      }
    }

  };

  return (
    <div>
      {
        successMessage ? (
          <span className="alert alert__success">{successMessage}</span>
        ) : errorMessage ? (
          <span className="alert alert__error">{errorMessage} Please sign in
            <Link
              to={`/join/login`}
              role="tab"
            >
            here.
            </Link>
          </span>
        ) : (
          <>
            <div className="form-text">
              <h1>Login to the LCSR Community</h1>
              <p>Do not have an account? <Link
                to="/join/register"><strong>Register here.</strong></Link></p>
            </div>
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
                {errors.username && <small className="alert alert__error">{errors.username}</small>}
              </div>

              <div className="form-row">
                <label htmlFor="password">
                  Password
                </label>

                <input
                  type="password"
                  ref={focusInputRef}
                  id="password"
                  name="password"
                  value={formState.password}
                  onChange={handleInputChange}
                  required
                />
                {errors.password && <small className="alert alert__error">{errors.password}</small>}
              </div>
              <div className="form-row">
                <button className="btn btn__register" type="submit">Login</button>
              </div>
            </form>
          </>
        )
      }
    </div>

  );
};

export default LoginForm;