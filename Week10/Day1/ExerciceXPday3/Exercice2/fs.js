const fs = require('fs');

fs.writeFile('newfile.txt', 'Hello, World!', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File created and written to successfully!');
});



fs.appendFile('newfile.txt', '\nBuy orange juice', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('Text appended to the file successfully!');
});



fs.unlink('newfile.txt', (err) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('File deleted successfully!');
});