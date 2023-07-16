const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/aboutMe/:hobby', (req, res) => {
  const hobby = req.params.hobby;

  if (typeof hobby === 'string') {
    res.send(hobby);
  } else {
    res.status(404).send('Invalid hobby');
  }
});

app.get('/pic', (req, res) => {
  res.sendFile(__dirname + '/public/image.html');
});

app.get('/form', (req, res) => {
  res.sendFile(__dirname + '/public/form.html');
});

app.post('/formData', (req, res) => {
  const email = req.body.email;
  const message = req.body.message;

  res.send(`${email} sent you a message: "${message}"`);
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000/');
});
