const http = require('http');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.write('<h1>Hello</h1>');
  res.write('<p>This is a paragraph.</p>');
  res.write('<div>Welcome to my server!</div>');
  res.end();
});

server.listen(3000, () => {
  console.log('Server is running on http://localhost:3000/');
});