// Exercice 6

// 6.2
const navBarElement = document.getElementById("navBar");
navBarElement.setAttribute("id", "socialNetworkNavigation");

// 6.3
const ulElement = document.querySelector("#socialNetworkNavigation ul");

const newLiElement = document.createElement("li");

const textNode = document.createTextNode("Logout");

newLiElement.appendChild(textNode);

ulElement.appendChild(newLiElement);


// 6.4 
const ullElement = document.querySelector("#socialNetworkNavigation ul");

const firstLiElement = ullElement.firstElementChild;
const firstLinkText = firstLiElement.textContent;
console.log("First link text:", firstLinkText);

const lastLiElement = ullElement.lastElementChild;
const lastLinkText = lastLiElement.textContent;
console.log("Last link text:", lastLinkText);
