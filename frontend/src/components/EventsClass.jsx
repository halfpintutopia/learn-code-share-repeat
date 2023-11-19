import React, { Component } from "react";

class EventsClass extends Component {
  constructor(props) {
    super(props);
    // this.clickHandler = this.clickHandler.bind(this);
  }

  // the arrow function doesn't have its own this, they inherit this from the surrounding context, this will correctly refer to the component instance.
  clickHandler = () => {
    console.log(this, "Clicked the class button");
  };

  // clickHandler() {
  //   console.log(this, "Clicked the class button")
  // }

  render() {
    return (
      <div>
        <button onClick={this.clickHandler}>Click Me - Class Component</button>
      </div>
    );
  }
}

export default EventsClass;
