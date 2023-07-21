import express from "express";
import dotenv from 'dotenv';
import cors from "cors";
import u_router from "./routes/usersrouter.js";

const app = express();
app.use(cors());

//body-parse

app.use(express.urlencoded({extended: true}));
app.use(express.json())
dotenv.config()


app.listen(process.env.PORT|| 3005, ()=>{
    console.log('I am listening')
});

app.use('/users', u_router);