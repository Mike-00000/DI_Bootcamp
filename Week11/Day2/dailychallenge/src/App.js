import React, { useState } from "react";
import "./App.css"; 

const App = () => {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaScript", votes: 0 },
    { name: "Java", votes: 0 },
  ]);

  const handleVote = (languageName) => {
    setLanguages((prevLanguages) =>
      prevLanguages.map((language) =>
        language.name === languageName
          ? { ...language, votes: language.votes + 1 }
          : language
      )
    );
  };

  return (
    <div className="container">
      <h1>Vote Your Language!</h1>
      <div className="languages-container">
        {languages.map((language) => (
          <div key={language.name} className="language-rectangle">
            <p>
              <strong>{language.name}</strong>
            </p>
            <p>
              <strong>{language.votes}</strong>
            </p>
            <p>
              <button onClick={() => handleVote(language.name)}>Click Here</button>
            </p>
            
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
