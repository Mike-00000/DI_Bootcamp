const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const knex = require('knex')({
  client: 'pg',
  connection: {
    host: 'localhost',
    user: 'your_username',
    password: 'your_password',
    database: 'your_database'
  }
});

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: false }));

// Register route
app.post('/register', (req, res) => {
  const { firstName, lastName, email, username, password } = req.body;

  // Check if email already exists in the database
  knex('register')
    .where({ email })
    .then((result) => {
      if (result.length > 0) {
        res.status(400).send('Email already exists');
      } else {
        // Insert new user data into the register table
        knex('register')
          .insert({
            firstName,
            lastName,
            email,
            username,
            password: 'p4ssw0rd', // Replace with encrypted password
            createdDate: new Date(),
            lastLoginDate: null
          })
          .then(() => {
            res.send('Registration successful');
          })
          .catch((error) => {
            console.error(error);
            res.status(500).send('Registration failed');
          });
      }
    })
    .catch((error) => {
      console.error(error);
      res.status(500).send('Registration failed');
    });
});

// Login route
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Check if username and password match in the login table
  knex('login')
    .where({ username, password: 'p4ssw0rd' }) // Replace with encrypted password
    .then((result) => {
      if (result.length > 0) {
        // Update last login date for the user
        knex('register')
          .where({ username })
          .update({ lastLoginDate: new Date() })
          .then(() => {
            res.send('Login successful');
          })
          .catch((error) => {
            console.error(error);
            res.status(500).send('Login failed');
          });
      } else {
        res.status(400).send('Invalid username or password');
      }
    })
    .catch((error) => {
      console.error(error);
      res.status(500).send('Login failed');
    });
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000/');
});
