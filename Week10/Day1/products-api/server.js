// const express = require('express')
import express from "express";
import dotenv from "dotenv";
import prouter from "./routes/products.js";
import path from "path";
import ejs from "ejs";

const app = express();
dotenv.config();

app.set('view engine', 'ejs');

const __dirname = path.resolve();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use("/", express.static(__dirname + "/public"));

app.listen(process.env.PORT, () => {
  console.log(`run on port ${process.env.PORT}`);
});

app.use("/api/products", prouter);
