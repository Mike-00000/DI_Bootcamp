

// Daily Challenge - HTML Form


// function handleSubmit() {
//     const firstName = document.getElementById('firstName').value;
//     const lastName = document.getElementById('lastName').value;
    
//     const data = {
//       name: firstName,
//       lastname: lastName
//     };
    
//     const jsonOutput = JSON.stringify(data);
//     document.getElementById('output').textContent = jsonOutput;
//   }

// __________________________

document.getElementById('sendButton').addEventListener('click', function() {
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    
    const data = {
      name: firstName,
      lastname: lastName
    };
    
    const jsonData = JSON.stringify(data);
    document.getElementById('output').textContent = jsonData;
  });
  