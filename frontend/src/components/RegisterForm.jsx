import React, { useRef, useState } from 'react';

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

const api = 'http://localhost:8000/api/users';
const emailRegex = /\\S+@\\S+\\.\\S+/;
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{16,}$/;


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
    } else if (!passwordRegex.test(formState.email)) {
      formIsValid = false;
      newErrors.password = "Email is not secure";
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
        const response = await fetch(api, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formState)
        });
        if (!response.ok) {
          const errorData = await response.json();
          setErrorMessage(errorData.detail);
        } else {
          setSuccessMessage('You have successfully created an account, please ');
        }

      } catch (error) {
        console.error(error);
        setErrorMessage(('An unexpected error occurred.'));
      }
    }

    setFormState(initialRegisterFormModalData);
  };

  return (
    <div>
      {
        successMessage ? (
          <div>{successMessage}</div>
        ) : errorMessage ? (
          <div>{errorMessage}</div>
        ) : (
          <>
            <h1>Join the LCSR Community</h1>
            <p>Have an account already? <b>Sign in</b></p>
            <form onSubmit={handleSubmit}>
              <div className="form-row">
                <label htmlFor="username">Username</label>
                {errors.username && <div>{errors.username}</div>}
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

              {errors.email && <div>{errors.email}</div>}
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

              {errors.password && <div>{errors.password}</div>}
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