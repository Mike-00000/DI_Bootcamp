function printStars(rows) {
    let pattern = '';
    for (let i = 1; i <= rows; i++) {
      pattern += '* '.repeat(i) + '\n';
    }
    console.log(pattern);
  }
  
  printStars(6);

  
function printStars(rows) {
for (let i = 1; i <= rows; i++) {
    let pattern = '';
    for (let j = 1; j <= i; j++) {
    pattern += '* ';
    }
    console.log(pattern);
}
}

printStars(6);
  