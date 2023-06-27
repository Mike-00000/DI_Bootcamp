
// EXERCICE XP

// _________________________________________
// Exercise 1 : Colors
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

// for (let i = 0; i < colors.length; i++) {
//   console.log(`${i + 1}# choice is ${colors[i]}.`);
// }

// if (colors.includes("Violet")) {
//     console.log("Yeah");
//   } else {
//     console.log("No...");
//   }
  


// _________________________________________
// Exercise 2 : Colors #2
// const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
// const ordinal = ["th","st","nd","rd"];

// for (let i = 0; i < colors.length; i++) {
//     let ordinalIndex = i+1;
//     let ordinalSuffix = 
//         ordinalIndex > 3 ? ordinal[0] : ordinal[ordinalIndex];
//     console.log(`${ordinalIndex} ${ordinalSuffix} choise is ${colors[i]}`);
// }



// _________________________________________
// Exercise 3 : Analyzing
// 1. 
// Output: ["bread", "carrot", "potato", "chicken", "apple", "orange"]

// 2.
// Output: ["U", "S", "A"]

// 3.
// Output: [undefined, undefined]




// _________________________________________
// Exercise 4 : Employees
// const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
//              { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
//              { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
//              { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
//              { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
//              { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
//              { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];
// const fname = users.map((element) => element["firstName"])
// const welcomeName = users.map(user => `Hello ${user.firstName}`)
// console.log(fname);
// console.log(welcomeName);

// const fullStackResidents = users.filter(user => user.role === 'Full Stack Resident');
// console.log(fullStackResidents);

// const fullStackResidentLastNames = fullStackResidents.map(user => user.lastName);
// console.log(fullStackResidentLastNames);




// _________________________________________
// Exercise 6 : Star Wars
// const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
// const epicString = epic.reduce((accumulator, currentValue) => accumulator + ' ' + currentValue);
// console.log(epicString);




// _________________________________________
// Exercise 7 : Employees #2
// const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
//                {name: "Liam", course: "Computer Science", isPassed: false}, 
//                {name: "Jenner", course: "Information Technology", isPassed: true}, 
//                {name: "Marco", course: "Robotics", isPassed: true}, 
//                {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
//                {name: "Jamie", course: "Big Data", isPassed: false}];

// const StudentIsPassed = students.filter(students => students.isPassed);
// StudentIsPassed.forEach(students => {
//     console.log(`Good job ${students.name}, you passed the course in ${students.course}`);
// })


