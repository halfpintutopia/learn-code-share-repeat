import React from "react";

const ConditionalRenderingFunctional = (props) => {
  return (
    <div>
      <h1>{props.connected ? "Connected" : "Not connected"}</h1>
    </div>
  );
};

export default ConditionalRenderingFunctional;
