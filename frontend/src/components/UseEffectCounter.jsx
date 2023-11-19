import React, { useState, useEffect } from "react";

const UseEffectCounter = () => {
  const [count, setCount] = useState(0);
  const [time, setTime] = useState(0);

  useEffect(() => {
    document.title = `${count}`;
  }, [count]);

  useEffect(() => {
    console.log("Creating timer");
    const interval = setInterval(() => {
      console.log("Interval executed");
      setTime((time) => time + 1);
    }, 1000);

    // Clear when the component is unmounted or re-rendered to avoid memory leaks and unexpected behaviour
    return () => {
      console.log("Clearing timer");
      clearInterval(interval);
    };
  }, []);

  const incrementValue = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <button onClick={incrementValue}>Increment Count ({count})</button>
      <h2>Time is {time}</h2>
    </div>
  );
};

export default UseEffectCounter;
