import React from "react";

class StatefulGreetingComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      introduction: "Hello!",
      buttonText: "Exit",
      count: 0,
    };
  }

  handleClick() {
    // prevState is automatically provided by React
    this.setState(
      (prevState) => ({
        introduction:
          prevState.introduction === "Hello!" ? "Goodbye!" : "Hello!",
        buttonText: prevState.buttonText === "Exit" ? "Enter" : "Exit",
      }),
      () => {
        // must run after setState has finished REMEMBER ASYNC
        console.log(this.state.introduction);
        console.log(this.state.buttonText);
      },
    );
  }

  incrementByOne() {
    this.setState(
      (prevState) => ({
        count: prevState.count + 1,
      }),
      () => {
        console.log(this.state.count);
      },
    );
  }

  incrementByFive() {
    this.incrementByOne();
    this.incrementByOne();
    this.incrementByOne();
    this.incrementByOne();
    this.incrementByOne();
  }

  render() {
    return (
      <div>
        <h1>
          {this.state.introduction} {this.props.name} {this.props.greeting}
        </h1>
        {/*Potential performance issue with this patter on the onClick, the new function is created every time the component renders, which can lead to unnecessary re-renders if the function is pass as a prop to child components */}
        <button onClick={() => this.handleClick()}>
          {this.state.buttonText}
        </button>
        <button onClick={() => this.incrementByFive()}>+ 5</button>

        <p>You have clicked {this.state.count} times</p>
      </div>
    );
  }
}

export default StatefulGreetingComponent;
