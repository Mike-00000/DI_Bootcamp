// Exercises XP

// ________________________________________________________
// Exercise 1 : Scope
// ________________________________________________________

// #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// // #1.1 - run in the console:
// funcOne()

/////////////////////// It will be 3. Because it's a closure function so the variable is saved.

// #1.2 What will happen if the variable is declared 
// with const instead of let ?

/////////////////////// It will bug. Const is a constant variable



//#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }
 

// // // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()
/////////////////////// It will be 0 because it's not a closure function so what inside disapear after the end of the function.
/////////////////////// It passes to 5
/////////////////////// it is 5

// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?
/////////////////////// It will bug. Const is a constant variable




// //#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()
/////////////////////// It will be "hello" because funcFour() defined a as "hello" as a global variable.




// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }
/////////////////////// It will be "test".



// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?
/////////////////////// It will be 1



// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
/////////////////////// It will be 2 because the default Boolean in JS is false
// alert(`outside of the if block ${a}`);
/////////////////////// It will be 2

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?
/////////////////////// It will be 2




// ________________________________________________________
// Exercise 2 : Ternary Operator
// ________________________________________________________

// const winBattle = () => true;

// const experiencePoints = winBattle() ? 10 : 1;
// console.log(experiencePoints);





// ________________________________________________________
// Exercise 3 : Is It A String ?
// ________________________________________________________

// const isString = (value) => {
//     return typeof value === 'string';
// };
  
// console.log(isString('hello')); 
// console.log(isString([1, 2, 4, 0])); 




// ________________________________________________________
// Exercise 4 : Find The Sum
// ________________________________________________________

// const funcAddition = (num1, num2) => num1 + num2
// console.log(funcAddition(5,8))
// console.log(funcAddition(13,80))




// ________________________________________________________
// Exercise 5 : Kg And Grams
// ________________________________________________________

// let w = []

// function weight (kilos) {
//     let wk = w + kilos;
//     let wg = wk*1000;
//     console.log(`${kilos}kg is equal to ${wg}g`)
// }

// const weight2 = function (kilos) {
//     let wk = w + kilos;
//     let wg = wk*1000;
//     console.log(`${kilos}kg is equal to ${wg}g`)
// }

// const weight3 = kilos => console.log(kilos * 1000);

// weight(1)
// weight2(1)
// weight3(1)




// ________________________________________________________
// Exercise 6 : Fortune Teller
// ________________________________________________________

// (function (numChildren, partnersname, location, job) {
//     console.log(`You will be a ${job} in ${location}, and married to ${partnersname} with ${numChildren} kids.`)
// })(4, "Elodie", "London", "fireman");




// ________________________________________________________
// Exercise 7 : Welcome
// ________________________________________________________

// (function (username) {
//     const navbar = document.getElementById('navbar');

//     const profileDiv = document.createElement('div');
//     profileDiv.className = 'profile';

//     const profileImg = document.createElement('img');
//     profileImg.className = 'profile-img';
//     profileImg.src = 'Bald_Eagle.jpg'; 

//     const usernameSpan = document.createElement('span');
//     usernameSpan.textContent = username;

//     profileDiv.appendChild(profileImg);
//     profileDiv.appendChild(usernameSpan);

//     navbar.appendChild(profileDiv);


// })("Mick");




// ________________________________________________________
// Exercise 8 : Juice Bar
// ________________________________________________________

// Part 1
// function makeJuice(size) {
//     function addIngredients(ingredient1, ingredient2, ingredient3) {
//       const outputDiv = document.getElementById('output');
//       const sentence = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}`;
//       outputDiv.textContent = sentence;
//     }
  
//     addIngredients('apple', 'orange', 'carrot');
//   }
  
// makeJuice('medium');


// Part 2

// function makeJuice(size) {
//     const ingredients = [];
  
//     function addIngredients(ingredient1, ingredient2, ingredient3) {
//       ingredients.push(ingredient1, ingredient2, ingredient3);
//     }
  
//     function displayJuice() {
//       const outputDiv = document.getElementById('output');
//       const sentence = `The client wants a ${size} juice, containing ${ingredients.join(', ')}`;
//       outputDiv.textContent = sentence;
//     }
  
//     addIngredients('apple', 'orange', 'carrot');
//     addIngredients('strawberry', 'banana', 'pineapple');
//     displayJuice();
//   }
  
// makeJuice('medium');		
  
