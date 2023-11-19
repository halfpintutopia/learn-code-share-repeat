import React, { Component } from "react";

class ClassCounter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
    };
  }

  incrementValue = () => {
    this.setState((prevState) => ({
      count: prevState.count + 1,
    }));
  };

  componentDidMount() {
    document.title = this.state.count;
  }

  componentDidUpdate() {
    document.title = this.state.count;
  }

  render() {
    return (
      <div>
        <button onClick={this.incrementValue}>
          Increment Count ({this.state.count})
        </button>
      </div>
    );
  }
}

export default ClassCounter;
