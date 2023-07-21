import express from 'express';
import { _register } from '../controllers/userController.js';

const u_router = express.Router();

u_router.post('/register', _register)

export default u_router