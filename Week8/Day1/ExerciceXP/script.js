
// // Exercises XP

// // Exercise 1 : Change The Article
// const queryh1 = document.querySelector("h1");
// console.log(queryh1)

// const lastp = document.body.firstElementChild.lastElementChild;
// console.log(lastp)

// const coloh2 = document.getElementById("h2s");
// coloh2.addEventListener("click", changeColor);
// function changeColor(event) {
//     event.target.style.backgroundColor = "red";
// }

// const hideH3 = document.getElementById("hideh3");
// hideH3.addEventListener("click", hiddenh3);
// function hiddenh3(event) {
//     event.target.style.visibility= "hidden";
// }

// const pbold = document.getElementsByTagName("p");
// const btnbold = document.getElementById("btn_bold");
// btnbold.addEventListener("click", changeBold);
// function changeBold(event) {
   
//         for (let p of pbold) {
//             p.style.fontWeight = "bold";
//         }
// }



// // Exercise 2 : Work With Forms
// const form = document.querySelector('form');
// const fnameInput = document.querySelector('#fname');
// const lnameInput = document.querySelector('#lname');

// let ul = document.querySelector('.usersAnswer');
// if (!ul) {
//   ul = document.createElement('ul');
//   ul.classList.add('usersAnswer');
//   document.body.appendChild(ul);
// }

// form.addEventListener('submit', (event) => {
//   event.preventDefault();

//   const fname = fnameInput.value;
//   const lname = lnameInput.value;

//   if (fname === '' || lname === '') {
//     return;
//   }

//   let li = document.createElement('li');
//   li.textContent = `first name: ${fname}`;
//   ul.appendChild(li);

//   li = document.createElement('li');
//   li.textContent = `last name: ${lname}`;
//   ul.appendChild(li);
// });


// Exercise 3 : Transform The Sentence
// let allBoldItems = [];
// const pstrong = document.getElementsByTagName("strong");
// function getBoldItems() {
//     for (let word of pstrong) {
//         allBoldItems.push(word) ;
//         console.log(allBoldItems)
//     }
// }
// getBoldItems()

// function highlight() {
//     for (let i = 0; i < allBoldItems.length; i++) {
//         allBoldItems[i].style.color = "blue";
//     }
// }
// // highlight()

// function returnItemsToDefault() {
//     for (let i = 0; i < allBoldItems.length; i++) {
//         allBoldItems[i].style.color = "black";
//     }
// }
// // returnItemsToDefault()

// function handleMouseOver() {
//     highlight();
//   }
  
// function handleMouseOut() {
//     returnItemsToDefault();
//   }
  
// var paragraph = document.querySelector('p');
  
// paragraph.addEventListener('mouseover', handleMouseOver);
  
// paragraph.addEventListener('mouseout', handleMouseOut);



// Exercice 5 : Event Listeners
const element = document.getElementById('myElement');

element.addEventListener('click', function() {
    element.style.backgroundColor = 'blue';
});

element.addEventListener('mouseover', function() {
    element.style.fontSize = '50px';
});

element.addEventListener('mouseout', function() {
    element.style.fontSize = '20px';
});

element.addEventListener('dblclick', function() {
    const randomX = Math.floor(Math.random() * window.innerWidth);
    const randomY = Math.floor(Math.random() * window.innerHeight);
    element.style.position = 'absolute';
    element.style.left = randomX + 'px';
    element.style.top = randomY + 'px';
});
