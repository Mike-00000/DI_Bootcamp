
// DAILY CHALLENGE - GO WILDCATS

const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
   ];

// 1.
const usernames = [];
gameInfo.forEach(function(player) {
  usernames.push(player.username + "!");
});
console.log(usernames);

// 2.
const winners = [];
gameInfo.forEach(function(player) {
    if (player.score > 5) {
        winners.push(player.username);
    }
})
console.log(winners);

// 3.
const sumScore = gameInfo.reduce((acc, currentValue) => {
    return acc+currentValue.score
}, 0)
console.log(sumScore)