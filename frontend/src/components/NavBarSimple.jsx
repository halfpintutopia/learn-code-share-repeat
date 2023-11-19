import css from "./css/NavBarSimple.module.css";

import React from "react";
import NavBarForm from "./NavBarForm";

class NavBarSimple extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      signIn: false,
      button: "Log in",
    };
  }

  handleSignIn = () => {
    this.setState((prevState) => ({
      signIn: !prevState.signIn,
      message:
        prevState.message === "Hello, guest!"
          ? "Welcome back, user!"
          : "Hello, guest!",
      button: prevState.button === "Login" ? "log out" : "log in",
    }));

    console.log(this);
  };

  render() {
    return (
      <div className={css.NavBar}>
        <h1>My Gallery</h1>

        <NavBarForm
          signIn={this.state.signIn}
          handleSignIn={this.handleSignIn}
        />
      </div>
    );
  }
}

export default NavBarSimple;
