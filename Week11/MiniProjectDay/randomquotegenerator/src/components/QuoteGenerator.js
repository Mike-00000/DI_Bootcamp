import React, { useState } from 'react';
import quotes from './quotes';

const getRandomColor = () => {
  return '#' + Math.floor(Math.random() * 16777215).toString(16);
};

const QuoteGenerator = ({ onButtonColorChange }) => {
  const [quote, setQuote] = useState('');
  const [author, setAuthor] = useState('');
  const [buttonColor, setButtonColor] = useState(getRandomColor());

  const generateRandomQuote = () => {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    const randomQuote = quotes[randomIndex];

    if (randomQuote.quote === quote) {
      generateRandomQuote();
      return;
    }

    setQuote(randomQuote.quote);
    setAuthor(randomQuote.author);
  };

  const handleButtonClick = () => {
    const newButtonColor = getRandomColor();
    setButtonColor(newButtonColor);
    onButtonColorChange(newButtonColor);
    generateRandomQuote();
  };

  return (
    <div
      style={{
        backgroundColor: 'white',
        padding: '20px',
        borderRadius: '25px',
        width: '700px',
        textAlign: 'center',
        color: 'black',
        fontWeight: 'bold',
      }}
    >
      <h1 style={{ color: buttonColor }}></h1>
      <h2 style={{ color: buttonColor }}>{quote}</h2>
      <p>{author}</p>
      <button
        onClick={handleButtonClick}
        style={{
          backgroundColor: buttonColor,
          padding: '10px 20px',
          border: 'none',
          borderRadius: '10px',
          cursor: 'pointer',
        }}
      >
        Generate Random Quote
      </button>
    </div>
  );
};

export default QuoteGenerator;
