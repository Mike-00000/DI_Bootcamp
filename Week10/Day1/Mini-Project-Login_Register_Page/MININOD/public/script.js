// script.js

document.addEventListener("DOMContentLoaded", () => {
  const registerForm = document.getElementById("registerForm");
  const loginForm = document.getElementById("loginForm");
  console.log(55555);
  // Listener pour la soumission du formulaire d'inscription
  registerForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(registerForm);
    const userData = {
      firstName: formData.get("firstName"),
      lastName: formData.get("lastName"),
      username: formData.get("username"),
      email: formData.get("email"),
      password: formData.get("password"),
    };

    try {
      const response = await fetch("http://localhost:3005/users/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });

      const data = await response.json();
      console.log(data);
      if (response.ok) {
        document.getElementById("registerSuccess").textContent = data.message;
      } else {
        document.getElementById("registerError").textContent = data.error;
      }
    } catch (error) {
      console.error("Error:", error);
      document.getElementById("registerError").textContent =
        "Une erreur est survenue lors de l'inscription";
    }
  });

  // Listener pour la soumission du formulaire de connexion
  loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(loginForm);
    const loginData = {
      username: formData.get("username"),
      password: formData.get("password"),
    };

    try {
      const response = await fetch("/users/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(loginData),
      });

      const data = await response.json();

      if (response.ok) {
        document.getElementById("loginSuccess").textContent = data.message;
      } else {
        document.getElementById("loginError").textContent = data.error;
      }
    } catch (error) {
      console.error("Error:", error);
      document.getElementById("loginError").textContent =
        "Une erreur est survenue lors de la connexion";
    }
  });
});
