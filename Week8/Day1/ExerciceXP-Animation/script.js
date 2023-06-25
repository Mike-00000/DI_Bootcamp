
// Exercises XP : Animations

// Exercise 1: Timer
setTimeout(function() {
    alert("Hello World");
}, 2000);


setTimeout(function() {
    var container = document.getElementById('container');
    var paragraph = document.createElement('p');
    paragraph.textContent = "Hello World";
    container.appendChild(paragraph);
}, 2000);


const container = document.getElementById('container');
const clearButton = document.getElementById('clear');

let interval = setInterval(function() {
    const paragraphs = container.getElementsByTagName('p');
    if (paragraphs.length < 5) {
        const paragraph = document.createElement('p');
        paragraph.textContent = "Hello World";
        container.appendChild(paragraph);
    } else {
        clearInterval(interval);
    }
}, 2000);

clearButton.addEventListener('click', function() {
    clearInterval(interval);
});

