function sing99Bottles() {
  let numBottles = prompt("With how many bottles do you want to start? ");
  let bottlesToTake = 1;

  while (numBottles > 0) {
    console.log(numBottles + " bottles of beer on the wall");
    console.log(numBottles + " bottles of beer");
    console.log("Take " + bottlesToTake + " down, pass them around");

    numBottles -= bottlesToTake;
    bottlesToTake++;

    console.log(numBottles + " bottles of beer on the wall\n");
  }
}

sing99Bottles();
