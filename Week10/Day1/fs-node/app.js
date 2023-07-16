const fs = require("fs").promises;

const read = async () => {
  try {
    const data = await fs.readFile("info.json", "utf-8");
    console.log(data);
  } catch (error) {
    console.log(error);
  }
};
read();

/*
  update info.json 
*/
// fs.readFile("info.json", "utf-8", (err, data) => {
//   if (err) return console.log(err);

//   const products = JSON.parse(data);
//   const index = products.findIndex((item) => item.id == 3);

//   products[index] = {
//     ...products[index],
//     price: 760,
//   };

//   fs.writeFile("info.json", JSON.stringify(products), "utf-8", (err) => {
//     if (err) return console.log(err);
//   });
// });

// console.log("before");

/*
  delete a file
*/
// fs.unlink("text.txt", (err) => {
//   if (err) return console.log(err);
// });

/*
  appendFile
*/

// const product = {
//   name: "iPhone",
//   price: 500,
// };

// fs.appendFile("info.json", JSON.stringify(product), "utf-8", (err) => {
//   if(err) return console.log(err);
// });

/*
  writeFile
*/

// const product = {
//   name: "iPad",
//   price: 1000,
// };
// fs.writeFile("text.txt", JSON.stringify(product), "utf-8", (err) => {
//   if (err) return console.log(err);
// });

/*
  readSync
*/
// fs.readFile('info.json','utf-8', (err, data) => {
//   if(err) return console.log(err);

//   console.log(data);
// })

/*
  readFileSync
*/
// try {
//   const data = fs.readFileSync("info.json", "utf-8");
//   console.log(JSON.parse(data));
// } catch (err) {
//   console.log(err);
// }
// console.log("after");
