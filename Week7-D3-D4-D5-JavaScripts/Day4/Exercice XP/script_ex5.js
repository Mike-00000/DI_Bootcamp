
// Exercise 5 : Users

// 2.1 
const containerDiv = document.getElementById("container");
console.log(containerDiv);


const listItems = document.querySelectorAll("li");
listItems.forEach(item => {
  if (item.textContent === "Pete") {
    item.textContent = "Richard";
  }
});


const secondList = document.querySelectorAll("ul.list")[1];
const secondListItem = secondList.querySelectorAll("li")[1];
secondListItem.remove();


const userList = document.querySelectorAll("ul.list");
userList.forEach(ul => {
  const firstListItem = ul.querySelector("li");
  firstListItem.textContent = "Michael";
});


// 3.
// 3.1 
const ulElements = document.querySelectorAll('ul');
ulElements.forEach((ul) => {
  ul.classList.add('student_list');
});

// 3.2 
const firstUl = document.querySelector('ul');
firstUl.classList.add('university', 'attendance');


document.addEventListener('DOMContentLoaded', function() {
    const divElement = document.getElementById('container');
    divElement.style.backgroundColor = 'lightblue';
    divElement.style.padding = '10px';
  
    const ulElements = document.querySelectorAll('ul.list');
    const danLiElement = ulElements[1].lastElementChild;
    danLiElement.style.display = 'none';
  
    const richardLiElement = ulElements[0].children[1];
    richardLiElement.style.border = '1px solid black';
  
    document.body.style.fontSize = '16px';
  });
  