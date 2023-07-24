

import React, { useState, useEffect } from "react";
import "./Color.css"; // Importez le fichier CSS pour les styles du composant

const Color = () => {
  const [favoriteColor, setFavoriteColor] = useState("red");

  useEffect(() => {
    alert("useEffect reached");
  }, []);

  const handleButtonClick = () => {
    setFavoriteColor("blue");
  };

  return (
    <div className="color-container">
      <h1>My favourite color is {favoriteColor}</h1>
      <button onClick={handleButtonClick}>Change Color to Blue</button>
    </div>
  );
};

export default Color;
