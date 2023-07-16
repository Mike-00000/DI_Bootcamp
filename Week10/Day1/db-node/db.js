const db = require("knex")({
  client: "pg",
  connection: {
    host: "lucky.db.elephantsql.com",
    port: "5432",
    user: "pbslqzln",
    database: "pbslqzln",
    password: "rqdux0deMFrWiILczRAreeqUJYSW-JNW",
  },
});

// db("products")
//   .update({ name: "p1111" })
//   .where({ id: 16 })
//   .del()
//   .returning("id")
//   .then((rows) => {
//     console.log(rows);
//   })
//   .catch((err) => {
//     console.log(err);
//   });
// 
db("products")
  .insert([
    { name: "user1", price: 11000 },
    // { name: "p2", price: 11000 },
  ])
  .returning("id")
  .then((rows) => {
    console.log(rows[0].id);
  })
  .catch((err) => {
    console.log(err);
  });

// db.select("id", "name", "price")
//   .where({ id: 3 })
//   .from("products")
//   .then((rows) => {
//     console.log(rows);
//   });

// db.raw("select name, price  from products where id = 3").then((rows) => {
//   console.log(rows.rows);
// });
