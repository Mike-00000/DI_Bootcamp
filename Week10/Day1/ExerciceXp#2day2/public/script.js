function fetchUserData() {
    fetch('/users')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        document.getElementById('result').textContent = JSON.stringify(data);
      });
  }