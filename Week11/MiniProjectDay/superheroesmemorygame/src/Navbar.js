import React from 'react';
import './App.css';

const Navbar = ({ currentScore, topScore }) => {
  return (
    <nav className='navbar'>
      <h1>Superheroes Memory Game</h1>
      <div className="score">
        <p>Current Score: {currentScore}</p>
        <p>Top Score: {topScore}</p>
      </div>
    </nav>
  );
};

export default Navbar;
