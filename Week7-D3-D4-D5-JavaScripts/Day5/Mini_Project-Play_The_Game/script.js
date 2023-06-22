// Exercise 1 : Play A Guessing Game
// First Part
function playTheGame() {
    if (confirm("would you like to play the game?") == true) {
        let userNumber = parseInt(prompt("enter a number between 0 and 10 "));
        if (userNumber < 1 || userNumber> 10) {
            alert("Sorry it’s not a good number, Goodbye")
        } 
        else if (isNaN(userNumber)) {
            alert("Sorry Not a number, Goodbye")
        } else {
            let computerNumber = Math.floor(Math.random() * 11);
            compareNumbers(userNumber,computerNumber);
        }
    } else {
        alert("No problem, Goodbye")
    }
}


// Second Part
function compareNumbers(userNumber,computerNumber) {
    console.log(userNumber,computerNumber)
        for (let i = 0 ; i < 2 ; i++) {
            if (userNumber == computerNumber) {
                alert("YOU WON!")
                return;
            } else if (userNumber > computerNumber) {
                alert("Your number is bigger than the computer’s, guess again");
                let userNumber = parseInt(prompt("enter a number between 0 and 10 "));
                if (i == 1) {
                    alert("You loose");
                } else continue;
                }
            else if (userNumber < computerNumber) {
                alert("Your number is smaller than the computer’s, guess again");
                let userNumber = parseInt(prompt("enter a number between 0 and 10 "));
                if (i == 1) {
                    alert("You loose");
                } else continue;
                } 
            }
    }
