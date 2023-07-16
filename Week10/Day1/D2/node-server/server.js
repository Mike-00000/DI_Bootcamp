const express = require("express");
const { products } = require("./config/data.js");

const app = express();

// parse application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }));

// parse application/json
app.use(express.json());

app.use('/', express.static(__dirname+'/public'))

app.get('/about', (req,res) => {
    res.sendFile(__dirname +'/public/about.html')
})

app.listen(3001, () => {
  console.log(`server is listneing on port 3001`);
});

// CRUD - Create - Read - Update - Delete
// Create - POST
// Read - GET
// Update - PUT
// Delete - DELETE

// Create - POST - create a product {"name":"IKey", "price":900}
app.post("/api/products", (req, res) => {
  console.log(req.body);
  products.push(req.body);
  res.json(products);
});

// Update - PUT - update one product - id as params, json as body
app.put("/api/products/:id", (req, res) => {
  const id = req.params.id;
  const index = products.findIndex((item) => item.id == id);
  if (index === -1) {
    return res.status(404).json({ msg: "not found" });
  }
  products[index] = {
    ...products[index],
    name: req.body.name,
    price: req.body.price,
  };
  res.json(products);
});

// Delete = delete a product - id as params
app.delete("/api/products/:id", (req, res) => {
  const id = req.params.id;
  const index = products.findIndex((item) => item.id == id);
  if (index === -1) {
    return res.status(404).json({ msg: "not found" });
  }
  products.splice(index, 1);
  res.json(products);
});

app.get("/api/products", (req, res) => {
  res.json(products);
});

// GET - get one product with id
app.get("/api/products/:product_id", (req, res) => {
  console.log(req.params);
  const productid = req.params.product_id;

  const product = products.find((item) => item.id == productid);
  if (!product) return res.status(404).json({ msg: "Product not found" });
  res.json(product);
});

// Read - GET searche a product with query ?name=ip
app.get("/api/search", (req, res) => {
  console.log(req.query);
  const name = req.query.name;
  const filtered = products.filter((item) => {
    return item.name.toLowerCase().includes(name.toLowerCase());
  });
  if (filtered.length === 0) {
    return res.status(404).json({ msg: "No product matched your search!!!" });
  }
  res.json(filtered);
});




