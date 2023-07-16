document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    var emailInput = document.getElementById('email');
    var messageInput = document.getElementById('message');
    var emailError = document.getElementById('emailError');
    var messageError = document.getElementById('messageError');
  
    emailError.textContent = '';
    messageError.textContent = '';
  
    if (!emailInput.value.match(/^\S+@\S+\.\S+$/)) {
      emailError.textContent = 'Invalid email address';
      return;
    }
  
    if (messageInput.value.trim() === '') {
      messageError.textContent = 'Message is required';
      return;
    }
  
    this.submit();
  });
  