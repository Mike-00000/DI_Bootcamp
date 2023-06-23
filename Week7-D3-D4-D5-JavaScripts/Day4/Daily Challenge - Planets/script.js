
// Daily Challenge: Planets

// 1.
const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

// 2.
const section = document.querySelector('.listPlanets');

// 3.
const colors = ['#BDBDBD', '#FFCEBF', '#2E86C1', '#FF7F50', '#D7BDE2', '#F7DC6F', '#AED6F1', '#5499C7'];

planets.forEach((planet, index) => {
    const div = document.createElement('div');
    div.classList.add('planet');
    div.style.backgroundColor = colors[index];
    section.appendChild(div);
  });
