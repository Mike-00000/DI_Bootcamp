import React, { useState, useEffect, useRef } from 'react';
import superheroesData from './superheroes.json';
import Card from './Card';
import Navbar from './Navbar';
import './App.css';

const App = () => {
  const [superheroes, setSuperheroes] = useState(superheroesData.superheroes);
  const [currentScore, setCurrentScore] = useState(0);
  const [topScore, setTopScore] = useState(0);
  const isFirstRender = useRef(true); // Ref to track the first render

  const shuffleCards = () => {
    setSuperheroes((prevSuperheroes) => {
      const shuffledSuperheroes = [...prevSuperheroes];
      for (let i = shuffledSuperheroes.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledSuperheroes[i], shuffledSuperheroes[j]] = [shuffledSuperheroes[j], shuffledSuperheroes[i]];
      }
      return shuffledSuperheroes;
    });
  };

  const handleCardClick = (id) => {
    setSuperheroes((prevSuperheroes) => {
      const updatedSuperheroes = prevSuperheroes.map((superhero) => {
        if (superhero.id === id) {
          if (!superhero.clicked) {
            return { ...superhero, clicked: true };
          } else {
            setCurrentScore(0);
            return { ...superhero, clicked: false };
          }
        }
        return superhero;
      });
      return updatedSuperheroes;
    });

    setCurrentScore((prevScore) => prevScore + 1);
  };

  useEffect(() => {
    if (isFirstRender.current) {
      isFirstRender.current = false;
      return;
    }
    shuffleCards();
  }, [currentScore]);

  return (
    <div className="App">
      <Navbar currentScore={currentScore} topScore={topScore} />
      <div className="card-container">
        {superheroes.map((superhero) => (
          <Card key={superhero.id} superhero={superhero} onClick={() => handleCardClick(superhero.id)} />
        ))}
      </div>
    </div>
  );
};

export default App;
