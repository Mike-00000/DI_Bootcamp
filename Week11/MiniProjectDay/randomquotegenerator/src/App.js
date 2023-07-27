import React, { useState } from 'react';
import QuoteGenerator from "./components/QuoteGenerator";
import "./App.css";

function App() {
  const [headerColor, setHeaderColor] = useState('red');

  return (
    <div className="App gradient-bg">
      <header className="App-header" style={{ backgroundColor: headerColor }}>
        <div>
          <QuoteGenerator onButtonColorChange={setHeaderColor} />
        </div>
      </header>
    </div>
  );
}

export default App;
