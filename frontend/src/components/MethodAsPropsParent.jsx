import React, { Component } from "react";

class MethodAsPropsParent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoggedIn: false,
    };
  }

  handleSignIn = () => {
    // this.setState({
    //   isLoggedIn: true
    // })
    // console.log(this);
    this.setState((prevState) => ({
      isLoggedIn: !prevState.isLoggedIn,
    }));
  };

  render() {
    return (
      <div>
        {this.state.isLoggedIn ? (
          <div>
            <p>Welcome to the site! Please complete the steps below:</p>
            <ol>
              <li>Confirm your email</li>
              <li>Complete your profile</li>
              <li>Subscribe to the newsletter</li>
            </ol>
            <button onClick={this.handleSignIn}>Sign out</button>
          </div>
        ) : (
          <div>
            <p>Please sign in</p>
            {/*When the button is clicked it updates*/}
            <button onClick={this.handleSignIn}>Sign in</button>
          </div>
        )}
      </div>
    );
  }
}

export default MethodAsPropsParent;
