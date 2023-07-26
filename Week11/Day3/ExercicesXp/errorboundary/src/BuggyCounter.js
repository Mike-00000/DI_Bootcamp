
import React, { useState } from "react";

const BuggyCounter = () => {
  const [counter, setCounter] = useState(0);

  const handleClick = () => {
    setCounter(counter + 1);
    if (counter === 4) {
      throw new Error("I crashed!");
    }
  };

  return (
    <div>
      <h3>Counter: {counter}</h3>
      <button onClick={handleClick}>Increment</button>
    </div>
  );
};

export default BuggyCounter;
