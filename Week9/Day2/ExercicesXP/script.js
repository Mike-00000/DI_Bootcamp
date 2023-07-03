
// Exercises XP

// ____________________________________________
// Exercise 1 : Comparison
function compareToTen (num) {
    return new Promise((resolve, reject) => {
        if (num <= 10) {
          resolve(`${num} is less than or equal to 10`);
        } else {
          reject(`${num} is greater than 10`);
        }
      });
    }    

compareToTen(15)
.then(result => console.log(result))
.catch(error => console.log(error));

compareToTen(8)
.then(result => console.log(result))
.catch(error => console.log(error));



// ____________________________________________
// Exercise 2 : Promises
const myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("success");
    }, 4000);
});

myPromise.then(result => console.log(result));



// ____________________________________________
// Exercise 3 : Resolve & Reject
const promise1 = Promise.resolve(3);
const promise2 = Promise.reject("Boo!");

promise1.then(result => console.log(result));
promise2.catch(error => console.log(error));
