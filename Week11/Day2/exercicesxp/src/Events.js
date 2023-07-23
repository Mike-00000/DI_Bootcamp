import React, { useState } from "react";

const Events = () => {
  const [isToggleOn, setIsToggleOn] = useState(true);

  const clickMe = () => {
    alert("I was clicked");
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      alert(`The Enter key was pressed, your input is ${event.target.value}`);
    }
  };

  const toggleState = () => {
    setIsToggleOn(!isToggleOn);
  };

  return (
    <div>
      <h1>localhost:3000 says</h1>
      <button onClick={clickMe}>OK button</button>
      <br />
      <input type="text" onKeyDown={handleKeyDown} />
      <br />
      <button onClick={toggleState}>{isToggleOn ? "on" : "off"}</button>
    </div>
  );
};

export default Events;
