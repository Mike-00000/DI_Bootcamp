const fs = require('fs');

fs.readFile('RightLeft.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const symbols = data.trim();
  let currentPosition = 0;
  let stepsToMinusOne = 0;

  for (let i = 0; i < symbols.length; i++) {
    if (symbols[i] === '>') {
      currentPosition++;
    } else if (symbols[i] === '<') {
      currentPosition--;
    }

    if (currentPosition === -1 && stepsToMinusOne === 0) {
      stepsToMinusOne = i + 1; // Add 1 because array index starts at 0
    }
  }

  console.log(`Final position: ${currentPosition} steps to the right.`);
  console.log(`Steps to hit position -1: ${stepsToMinusOne} steps.`);
});
