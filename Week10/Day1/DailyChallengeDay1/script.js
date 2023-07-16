const largeNumber = require('./main');
const b = 5;

const sum = largeNumber + b;
console.log(sum);


// const http = require('http');

// const server = http.createServer((req, res) => {
//   res.setHeader('Content-Type', 'text/html');
//   res.end('<p>My Module is ' + largeNumber + '</p><h1>Hi there at the frontend</h1>');
// });

// server.listen(3000);
// console.log("I'm listening");


const http = require('http');
const getCurrentDateTime = require('./main');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.end('<p>' + getCurrentDateTime() + '</p>');
});

server.listen(8080);
console.log("I'm listening");