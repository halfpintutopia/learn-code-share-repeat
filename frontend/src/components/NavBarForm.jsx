import React from "react";
import css from "./css/NavBarForm.module.css";

function NavBarForm(props) {
  return (
    <div className={css.NavBar}>
      {props.signIn ? (
        <form action="">
          <label htmlFor="username">Username</label>
          <input id="username" type="text" name="username" />

          <label htmlFor="password">Password</label>
          <input id="password" type="text" name="password" />

          <button onClick={props.handleSignIn}>Submit</button>
        </form>
      ) : (
        <button onClick={props.handleSignIn}>Login</button>
      )}
    </div>
  );
}

export default NavBarForm;
