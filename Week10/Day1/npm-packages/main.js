const axios = require("axios");
const bcrypt = require("bcrypt");

const hashPassword = async (pass) => {
  try {
    const salt = await bcrypt.genSalt(10);
    const hash = bcrypt.hashSync(pass, salt);
    console.log(hash);
  } catch (e) {
    console.log();
  }
};

hashPassword("12345678");

const user = async () => {
  try {
    const res = await axios.get("https://jsonplaceholder.typicode.com/users");
    console.log(res.data);
  } catch (err) {
    console.log(err);
  }
};

