import React from 'react';

const Card = ({ superhero, onClick }) => {
  return (
    <div className="card" onClick={() => onClick(superhero.id)}>
      <img src={superhero.image} alt={superhero.name} />
      <h2>{superhero.name}</h2>
      <p>{superhero.occupation}</p>
    </div>
  );
};

export default Card;
