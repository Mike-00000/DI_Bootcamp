// Exercise 1 : List Of People
// Part I - Review About Arrays

// let people = ["Greg", "Mary", "Devon", "James"];
// console.log(people)

// // 1.
// people.shift();
// console.log(people)

// // 2.
// people[3] = "Jason";
// console.log(people)

// // 3.
// people.push("Michael");
// console.log(people)

// // 4.
// let peopleMary = people
// let getMary = peopleMary.indexOf("Mary")
// console.log(getMary)

// // 5.
// let copyPeople = people.slice(1,4);
// console.log(copyPeople)

// // 6.
// console.log(people.indexOf("Foo"))
// // -1 because it doesn't exist

// // 7.
// let last = people[4]
// console.log(last)


// Part II - Loops

// 1.
// for(let i = 0; i < people.length; i++){
//   console.log(people[i]);
// }

// 2.
// for (let i = 0; i < people.length; i++) {
//     console.log(people[i]);
  
//     if (people[i] === "Devon") {
//       break;
//     }
//   }



// // Exercise 2 : Your Favorite Colors
// let colors = ["blue", "black", "pink", "red", "grey"];
// for (let index = 0; index < colors.length; index++) {
//     let sentence = `My #${index+1} color is ${colors[index]}`;
//     console.log(sentence);
// }


// Exercise 3 : Repeat The Question
// 1.
// const userInput = prompt("Please enter a number:");
// const type = typeof userInput;

// console.log("The data type of the input is:", type);


// 2.
// let number = prompt("Please enter a number:");

// while (Number(number) < 10) {
//   number = prompt("Please enter a new number:");
// }

// console.log("The number is greater than or equal to 10.");



// Exercise 4 : Building Management
// 1.
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }

// // 2.
// console.log("Number of floors in the building:", building.numberOfFloors);

// // 3.
// console.log("Number of apartments on the first floor:", building.numberOfAptByFloor.firstFloor);
// console.log("Number of apartments on the third floor:", building.numberOfAptByFloor.thirdFloor);

// // 4.
// const secondTenant = building.nameOfTenants[1];
// const roomsForSecondTenant = building.numberOfRoomsAndRent.dan[0];

// console.log("Second tenant:", secondTenant);
// console.log("Number of rooms in second tenant's apartment:", roomsForSecondTenant);

// // 5.
// const sarahRent = building.numberOfRoomsAndRent.sarah[1];
// const davidRent = building.numberOfRoomsAndRent.david[1];
// const danRent = building.numberOfRoomsAndRent.dan[1];

// if (sarahRent + davidRent > danRent) {
//     building.numberOfRoomsAndRent.dan[1] = 1200;
// }

// console.log("Dan's updated rent:", building.numberOfRoomsAndRent.dan[1]);
  


// Exercise 5 : Family
// const family = {
//     mother:"Sarah", 
//     father:"Abraham", 
//     son:"Isaac"
// };

// for (let key in family){
//     console.log(key); //key
// }

// for (let key in family){
//     console.log(family[key]); //value
// }