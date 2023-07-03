
// EXERCICE XP


// ________________________________________________________
// Exercise 1 : HTML Form                                  |
// 1.3                                                     |
// The data will be sent in the URL                        |
//                                                         |
//                                                         |
//                                                         |
// ________________________________________________________|
// Exercise 2 : HTML Form #2                               |
// 2.3                                                     |
// The data will be sent in the body (payload)             |
//                                                         |
//                                                         |
//                                                         |
// ________________________________________________________|
// Exercise 3 : JSON Mario

const marioGame = {
    detail : "An amazing game!",
    characters : {
        mario : {
          description:"Small and jumpy. Likes princesses.",
          height: 10,
          weight: 3,
          speed: 12,
        },
        bowser : {
          description: "Big and green, Hates princesses.",
          height: 16,
          weight: 6,
          speed: 4,
        },
        princessPeach : {
          description: "Beautiful princess.",
          height: 12,
          weight: 2,
          speed: 2,
        }
    },
  }

// 3.1
// const marioStringify = JSON.stringify(marioGame);
// console.log(marioStringify);
// It appears not clear

// 3.2
const marioStringify = JSON.stringify(marioGame, null, 2);
console.log(marioStringify);

// 3.3