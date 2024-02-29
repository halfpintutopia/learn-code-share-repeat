import { Link } from "react-router-dom";
import { useRef, useState } from "react";
import { resetPassword } from "../utils/api";

const ResetForm = () => {
  const focusInputRef = useRef(null);
  const [ resetEmail, setResetEmail ] = useState('');
  const [ errorMessage, setErrorMessage ] = useState('');

  const handleInputChange = (event) => {
    event.preventDefault();
    const value = event.target.value;
    setResetEmail(value);
  };



  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log('formState', resetEmail);

    try {
      const response = await resetPassword(resetEmail);
      console.log(response);

      if (response.ok) {
        // navigate('/');
        // window.location.href = '/';
      }

    } catch (error) {
      console.error(error);
      setErrorMessage(`An unexpected error occurred: ${ error }`);
    }
  };

  return (
    <>
      <div className="form-text">
        <h1 className="form-header">Reset your password</h1>
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
          <label htmlFor="email">Email</label>

          <input
            type="text"
            ref={ focusInputRef }
            id="email"
            name="email"
            value={ resetEmail }
            onChange={ handleInputChange }
            placeholder="Email"
            required
          />
        </div>

        <div className="form-row">
          <button className="btn btn__register" type="submit">Reset</button>
        </div>
      </form>
    </>
  );
};

export default ResetForm;