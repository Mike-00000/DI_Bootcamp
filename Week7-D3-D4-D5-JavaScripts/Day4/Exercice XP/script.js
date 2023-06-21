

// Exercise 1 : Find The Numbers Divisible By 23
// let sum = 0;
// function displayNumbersDivisible(number) {
//     for(let i = 0; i < 500; i++){
//         if (i % number === 0) {
//             console.log(i);
//             sum += i;
//         }
//     }
// }

// displayNumbersDivisible(23)
// console.log(sum)



// _______________________________________
// Exercise 2 : Shopping List
// const stock = {
//   banana: 6,
//   apple: 0,
//   pear: 12,
//   orange: 32,
//   blueberry: 1,
// };

// const prices = {
//   banana: 4,
//   apple: 2,
//   pear: 1,
//   orange: 1.5,
//   blueberry: 10,
// };

// const shoppingList = ["banana", "orange", "apple"];

// let totalPrice = 0;

// function myBill(shoppingList) {
//   for (let item of shoppingList) {
//     if (stock[item] > 0) {
//         totalPrice += prices[item];
//         stock[item] -= 1
//     }
//   }
// }

// myBill(shoppingList);
// console.log(totalPrice);



// _______________________________________
// Exercise 3 : What’s In My Wallet ?

// function changeEnough(itemPrice, amountOfChange) {
//     const quarterValue = 0.25;
//     const dimeValue = 0.10;
//     const nickelValue = 0.05;
//     const pennyValue = 0.01;
  
//     const totalChange = (amountOfChange[0] * quarterValue) + (amountOfChange[1] * dimeValue) + (amountOfChange[2] * nickelValue) + (amountOfChange[3] * pennyValue);
  
//     return totalChange >= itemPrice;
//   }
  
// console.log(changeEnough(5, [2, 10, 5, 9]));
// console.log(changeEnough(10, [20, 100, 0, 5]));
// console.log(changeEnough(3, [0, 0, 20, 5]));
  


// ____________________________________________
// Exercise 4 : Vacations Costs

// 4.1
// function hotelCost() {
//     let numberOfNights = 0;
    
//     while (true) {
//       let input = prompt("Enter the number of nights you would like to stay in the hotel:");
      
//       if (input === null || isNaN(input)) {
//         continue;
//       }
      
//       numberOfNights = parseInt(input);
//       break;
//     }
    
//     const hotelPricePerNight = 140;
//     const totalPrice = numberOfNights * hotelPricePerNight;
    
//     return totalPrice;
//   }
  
// // const hotelTotal = hotelCost();
// // console.log("Total hotel cost:", hotelTotal);


// // 4.2
// function planeRideCost() {
//     let destination = "";
  
//     while (true) {
//       let input = prompt("Enter your destination:");
  
//       if (input === null || typeof input !== "string") {
//         continue;
//       }
  
//       destination = input.toLowerCase();
//       break;
//     }
  
//     let price = 0;
  
//     if (destination === "london") {
//       price = 183;
//     } else if (destination === "paris") {
//       price = 220;
//     } else {
//       price = 300;
//     }
  
//     return price;
//   }
  
// //   const flightCost = planeRideCost();
// //   console.log("Flight cost:", flightCost);
  

// // 4.3
// function rentalCarCost() {
//     let numberOfDays = 0;
  
//     while (true) {
//       let input = prompt("Enter the number of days you would like to rent the car:");
  
//       if (input === null || isNaN(input)) {
//         continue;
//       }
  
//       numberOfDays = parseInt(input);
//       break;
//     }
  
//     const dailyRate = 40;
//     let totalCost = numberOfDays * dailyRate;
  
//     if (numberOfDays >= 10) {
//       totalCost -= totalCost * 0.05;
//     }
  
//     return totalCost;
//   }
  
// // const carRentalTotal = rentalCarCost();
// // console.log("Total car rental cost:", carRentalTotal);


// // 4.4 / 4.5 / 4.6
// function totalVacationCost() {
//     const hotelPrice = hotelCost();
//     const planeTicketCost = planeRideCost();
//     const carRentalCost = rentalCarCost();
  
//     const totalCost = hotelPrice + planeTicketCost + carRentalCost;
  
//     console.log("The car cost: $" + carRentalCost);
//     console.log("The hotel cost: $" + hotelPrice);
//     console.log("The plane tickets cost: $" + planeTicketCost);
//     console.log("Total vacation cost: $" + totalCost);
  
//     return totalCost;
//   }
  
// totalVacationCost();


// ________________________________
// Exercise 5 : Users
