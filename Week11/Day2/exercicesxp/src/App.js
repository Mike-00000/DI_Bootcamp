import logo from './logo.svg';
import './App.css';
import React from "react";
import Car from "./Components/Car";
import Events from "./Events";
import Phone from "./Phone";
import Color from "./Colors";


const carinfo = { name: "Ford", model: "Mustang" };



const App = () => {
  return (
    <>
      <h2>Exercise 1: Car And Components</h2>
      <Car carinfo={carinfo} />

      <h2>Exercise 2: Events</h2>
      <Events />

      <h2>Exercice 3: Phone</h2>
      <Phone />

      <h2>Exercise 4: UseEffect Hook</h2>
      <Color />
    </>
  );
};

export default App;
