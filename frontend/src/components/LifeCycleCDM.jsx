import React, { Component } from "react";

import LifeCycleCDMChild from "./LifeCycleCDMChild";

class LifeCycleCDM extends Component {
  constructor(props) {
    console.log("constructor called");
    super(props);

    this.state = {
      data: "loading",
    };
  }

  getData() {
    console.log("getData() called");
    setTimeout(() => {
      console.log("data fetched");
      this.setState({
        data: "loaded!",
      });
    }, 3000);
  }

  componentDidMount() {
    console.log("component mounted");
    this.getData();
  }

  render() {
    console.log("render method");
    return (
      <div>
        <h1>Lifecycles</h1>
        <LifeCycleCDMChild />
      </div>
    );
  }
}

export default LifeCycleCDM;
