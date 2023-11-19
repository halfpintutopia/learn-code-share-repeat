import React from "react";

const EventsFunctional = () => {
  function clickHandler() {
    console.log("Clicked the functional button");
  }

  return (
    <div>
      <button onClick={clickHandler}>Click Me - Functional Component</button>
    </div>
  );
};

export default EventsFunctional;
