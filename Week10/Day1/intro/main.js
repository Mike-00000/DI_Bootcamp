const { usersInfo } = require("./usersInfo.js");

usersInfo().then((data) => {
  console.log(data);
});

const data = async() => {
    const ret = await usersInfo()
    console.log(ret);
    return 'zivuch'
}
data()
