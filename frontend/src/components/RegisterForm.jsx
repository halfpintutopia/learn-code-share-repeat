import React, { useRef, useState } from 'react';
import { Link } from "react-router-dom";
import { postData } from "./fetchData";

const initialRegisterFormModalData = {
  username: '',
  email: '',
  password: ''
};

const initialErrorState = {
  username: '',
  email: '',
  password: ''
};

const api = 'http://localhost:8000/api/users/register/';
const emailRegex = /\S+@\S+\.\S+/;
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W])[A-Za-z\d\W]{16,}$/;

const RegisterForm = () => {
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

    if (!formState.email) {
      formIsValid = false;
      newErrors.email = 'Email is required';
    } else if (!emailRegex.test(formState.email)) {
      formIsValid = false;
      newErrors.email = 'Email is not valid';
    }

    if (!formState.password) {
      formIsValid = false;
      newErrors.password = 'Password is required';
    } else {
      const testResult = passwordRegex.test(formState.password);
      if (!testResult) {
        formIsValid = false;
        newErrors.password = "Password is not secure";
      }
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
          setErrorMessage(errorData.username);
        } else {
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
              to={`/login`}
              role="tab"
            >
            here.
            </Link>
          </span>
        ) : (
          <>
            <div className="form-text">
              <h1>Join the LCSR Community</h1>
              <p>Have an account already? <Link
                to="/join/login"><strong>Sign in</strong></Link></p>
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
                {errors.email && <small className="alert alert__error">{errors.email}</small>}
              </div>


              <div className="form-row">
                <label htmlFor="password">
                  Password
                  <ul>
                    <li><small>Must be at least 16 characters</small></li>
                    <li><small>Must contain upper case letter</small></li>
                    <li><small>Must contain special characters</small></li>
                    <li><small>Must contain lower case letter</small></li>
                  </ul>
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
                <button className="btn btn__register" type="submit">Get Started</button>
              </div>
            </form>
          </>
        )
      }
    </div>

  );
};

export default RegisterForm;