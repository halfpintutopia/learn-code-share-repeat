import React, { Component } from "react";

class LifeCycleCDU extends Component {
  constructor(props) {
    console.log("Child constructor called");
    super(props);
    this.state = {
      greeting: "Child Hello!",
    };
  }

  updateGreeting = () => {
    console.log("Child update greeting called");
    this.setState((prevState) => {
      return {
        greeting:
          prevState.greeting === "Child Hello!"
            ? "Child Goodbye!"
            : "Child Hello!",
      };
    });
  };

  // updateGreeting = () => {
  //   this.setState(prevState => ({
  //     greeting: prevState.greeting === 'Hello' ? 'Goodbye' : 'Hello'
  //   }))
  // }

  componentDidUpdate(prevProps, prevState) {
    console.log("Child Component updated");
    console.log({ prevProps });
    console.log({ prevState });
    if (prevProps.parentGreeting !== this.props.parentGreeting) {
      console.log("Parent greeting has changed");
    }
  }

  render() {
    console.log("Child render method called");
    return (
      <div>
        <h1>{this.state.greeting}</h1>
        <button onClick={this.updateGreeting}>Update Greeting</button>
      </div>
    );
  }
}

export default LifeCycleCDU;
