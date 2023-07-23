import React, { useState } from "react";
import Garage from "./Garage";

const Car = ({ carinfo }) => {
  const [color, setColor] = useState("red");

  const changeColor = () => {
    setColor("blue");
  };

  return (
    <>
      <h1>This car is {color} {carinfo.model}</h1>
      <button onClick={changeColor}>Change Color</button>
      <Garage size="small" />
    </>
  );
};

export default Car;
