import { useRef, useState } from 'react';
import { Link, useNavigate } from "react-router-dom";
import { postData } from "../helpers/fetchData";
import { TOKEN_OBTAIN_API, TOKEN_REFRESH_API } from "../constants/constants";
import { fetchWithToken } from "../helpers/fetchWithToken";

const initialRegisterFormModalData = {
  username: '',
  password: ''
};

const initialErrorState = {
  username: '',
  password: ''
};

const LoginForm = () => {
  const navigate = useNavigate();
  const focusInputRef = useRef(null);
  const [ formState, setFormState ] = useState(initialRegisterFormModalData);
  const [ errors, setErrors ] = useState(initialErrorState);
  const [ errorMessage, setErrorMessage ] = useState('');

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
        const response = await fetchWithToken(TOKEN_OBTAIN_API, {
          method: 'POST',
          body: JSON.stringify(formState)
        });

        if (response.ok) {
          // navigate('/');
          window.location.href = '/';
        }

      } catch (error) {
        console.error(error);
        setErrorMessage(('An unexpected error occurred.'));
      }
    }
  };

  return (
    <>
      <div className="form-text">
        <h1 className="form-header">Login to the LCSR Community</h1>
        <p>Do not have an account? <Link
          to="/join/register"><strong>Register here.</strong></Link></p>
      </div>
      {
        errorMessage && (
          <span className="alert alert__error">
            <p>{ errorMessage }.
            Please sign in <Link to={ `/join/login` } role="tab">here.</Link></p>
          </span>
        )
      }
      <form onSubmit={ handleSubmit }>
        <div className="form-row">
          <label htmlFor="username">Username</label>

          <input
            type="text"
            ref={ focusInputRef }
            id="username"
            name="username"
            value={ formState.username }
            onChange={ handleInputChange }
            placeholder="Username"
            required
          />
          { errors.username && <small className="alert alert__error">{ errors.username }</small> }
        </div>

        <div className="form-row">
          <label htmlFor="password">
            Password
          </label>

          <input
            type="password"
            ref={ focusInputRef }
            id="password"
            name="password"
            value={ formState.password }
            onChange={ handleInputChange }
            placeholder="Password"
            required
          />
          { errors.password && <small className="alert alert__error">{ errors.password }</small> }
        </div>
        <div className="form-row">
          <button className="btn btn__register" type="submit">Login</button>
        </div>
      </form>
    </>
    // )
    // }
    // </div>
  );
};

export default LoginForm;