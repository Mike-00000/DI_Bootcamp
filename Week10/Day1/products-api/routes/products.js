import express from "express";
import {
  _getAllProducts,
  _getProduct,
  _searchProduct,
  _insertProduct,
  _updateProduct,
  _deleteProduct,
  _getAllProductsEjs,
} from "../controllers/products.js";

const prouter = express.Router();

prouter.get("/ejs/shop", _getAllProductsEjs);
prouter.get("/search", _searchProduct);
prouter.get("/", _getAllProducts);
prouter.get("/:id", _getProduct);
prouter.post("/", _insertProduct);
prouter.put("/:id", _updateProduct);
prouter.delete("/:id", _deleteProduct);

export default prouter;
