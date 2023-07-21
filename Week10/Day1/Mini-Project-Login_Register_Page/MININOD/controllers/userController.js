import {register} from "../models/users.js";
import bcrypt from 'bcrypt';

export const _register = async (req, res) => {
    const first_name = req.body.fname;
    const last_name = req.body.lname;
    const username = req.body.username;
    const email = req.body.email.toLowerCase();
    const password = req.body.password + "";

    const salt = bcrypt.genSaltSync(10);
    const hash = bcrypt.hashSync(password, salt);
    try {
        const rows = await register({first_name, last_name, username, email, hash});
        res.json(rows);
    } catch (err) {
        console.log(err);
        res.status(404).json({msg: err.message});
    }
};



