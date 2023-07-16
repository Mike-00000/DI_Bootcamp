const usersInfo = async () => {
  try {
    // const res = await fetch("https://jsonplaceholder.typicode.com/users");
    // const data = await res.json();
    return [1, 2, 3];
  } catch (err) {
    console.log(err);
  }
};

// console.log(usersInfo());

module.exports = {
  usersInfo,
};
