
// __________________________________CONVERTOR__________________________________

document.addEventListener('DOMContentLoaded', function() {
    console.log("form", document.getElementById("conversion-form"));
    document.getElementById("conversion-form").addEventListener("submit", function(event) {
      event.preventDefault();
  
      const subTopic = document.getElementById("sub-topic").value;
      const conversionObject = document.getElementById("conversion-object").value;
  
      let conversionRatio;
      let quantityWater;
      let conversionResult;
  
      if (subTopic === "bath") {
        if (conversionObject === "coffee-cup") {
          conversionRatio = 50;
        } else if (conversionObject === "water-bottle") {
            conversionRatio = 1000;
        } else if (conversionObject === "wine-glass") {
          conversionRatio = 150;
        } else if (conversionObject === "coke-can") {
          conversionRatio = 333;
        } else if (conversionObject === "vodka-shot") {
          conversionRatio = 30;
        }
        quantityWater = 130000;

      } else if (subTopic === "brushing") {
        if (conversionObject === "coffee-cup") {
          conversionRatio = 50;
        } else if (conversionObject === "water-bottle") {
            conversionRatio = 1000;
        } else if (conversionObject === "wine-glass") {
          conversionRatio = 150;
        } else if (conversionObject === "coke-can") {
          conversionRatio = 333;
        } else if (conversionObject === "vodka-shot") {
          conversionRatio = 30;
        }
  
        quantityWater = 3000;
      }
  
      conversionResult = Math.floor(quantityWater / conversionRatio);
  
      const resultContainer = document.getElementById("result-container");
      resultContainer.innerHTML =
        "The result of the conversion is : " +
        conversionResult +
        " " +
        conversionObject;
  


      // LOCALSTORAGE PART --- LOCALSTORAGE PART ---LOCALSTORAGE PART 
      const storedConversions = localStorage.getItem("conversions");
  
      // check if data in localStorage
      if (storedConversions) {
        const conversions = JSON.parse(storedConversions);
  
        // add new conversion to the list
        conversions.push({
          subTopic: subTopic,
          conversion: conversionObject,
          result: conversionResult,
        });
  
        // update of data in localStorage
        localStorage.setItem("conversions", JSON.stringify(conversions));
      } else {
        // if no data, it creates new list
        const conversions = [
          {
            subTopic: subTopic,
            conversion: conversionObject,
            result: conversionResult,
          },
        ];
  
        // save data in localStorage
        localStorage.setItem("conversions", JSON.stringify(conversions));
      }
  
      // update the table
      updateConversionTable();
      // update the sentence
      updateConversionSummary();
    });
  
    // update the table
    function updateConversionTable() {
      const conversionTable = document.getElementById("conversion-table");
      const tbody = conversionTable.querySelector("tbody");
  
      // supress
      tbody.innerHTML = "";
  
      // recup conversions from localStorage
      const storedConversions = localStorage.getItem("conversions");
  
      if (storedConversions) {
        const conversions = JSON.parse(storedConversions);
  
        for (const conversion of conversions) {
          const row = document.createElement("tr");
          const subTopicCell = document.createElement("td");
          const conversionObjectCell = document.createElement("td");
          const conversionResultCell = document.createElement("td");
  
          subTopicCell.textContent = conversion.subTopic;
          conversionObjectCell.textContent = conversion.conversion;
          conversionResultCell.textContent = conversion.result;
  
          row.appendChild(subTopicCell);
          row.appendChild(conversionObjectCell);
          row.appendChild(conversionResultCell);
  
          tbody.appendChild(row);
        }
      }
    }
  
    // update sentence
    function updateConversionSummary() {
      const conversionSummary = document.getElementById("conversion-summary");
      const summaryParagraph = conversionSummary.querySelector("p");
  
      // recup conversions from localStorage
      const storedConversions = localStorage.getItem("conversions");
  
      if (storedConversions) {
        const conversions = JSON.parse(storedConversions);
        const totalConversions = conversions.length;
  
        summaryParagraph.textContent = `You have made ${totalConversions} conversion(s). You will find their details below.`;
      } else {
        summaryParagraph.textContent = "No conversion performed.";
      }
    }
  
    updateConversionTable();
    updateConversionSummary();
  });
  
document.getElementById('reset-button').addEventListener('click', function() {
// reset
localStorage.removeItem('conversions');

location.reload();
});



// __________________________________WEATHER API__________________________________

document.getElementById("weather-button").addEventListener("click", function() {
    const cities = ["Paris", "Tel-Aviv", "New York", "London", "Tokyo", "Sydney"];
    const randomIndex = Math.floor(Math.random() * cities.length);
    const randomCity = cities[randomIndex];
  
    fetch(`https://api.weatherapi.com/v1/current.json?key=3931ba817b3d433380194100231207&q=${randomCity}`)
      .then(response => response.json())
      .then(data => {
        
        const cityName = data.location.name;
        const temperature = data.current.temp_c;
        const description = data.current.condition.text;
        const weatherData = {
          city: cityName,
          temperature: temperature,
          description: description
        };
  
        // for the historique
        let weatherHistory = localStorage.getItem("weatherHistory");
        if (weatherHistory) {
          weatherHistory = JSON.parse(weatherHistory);
        } else {
          weatherHistory = [];
        }
  
        // add meteo to historique
        weatherHistory.push(weatherData);
  
        // Stockage of the historique
        localStorage.setItem("weatherHistory", JSON.stringify(weatherHistory));
  
        // update of HTML with informations
        const weatherInfoElement = document.getElementById("weather-info");
        weatherInfoElement.innerHTML = `City : ${cityName}<br>Temperature : ${temperature}°C<br>Description : ${description}`;
  
        // display historique
        displayWeatherHistory(weatherHistory);
      })
      .catch(error => {
        console.error("Erreur lors de la récupération des informations météorologiques :", error);
      });
  });
  
  // to display historique meteo
  function displayWeatherHistory(weatherHistory) {
    const historyElement = document.getElementById("weather-history");
    historyElement.innerHTML = ""; // Réinitialiser l'affichage de l'historique
  
    weatherHistory.forEach(weatherData => {
      const city = weatherData.city;
      const temperature = weatherData.temperature;
      const description = weatherData.description;
  
      const weatherItem = document.createElement("div");
      weatherItem.innerHTML = `City : ${city}<br>Temperature : ${temperature}°C<br>Description : ${description}`;
      weatherItem.classList.add("weather-item");
  
      historyElement.appendChild(weatherItem);
    });
  }
  
  // récup historique
  document.addEventListener("DOMContentLoaded", function() {
    const weatherHistory = localStorage.getItem("weatherHistory");
    if (weatherHistory) {
      const parsedHistory = JSON.parse(weatherHistory);
      displayWeatherHistory(parsedHistory);
    }
  });
  

const resetButtons = document.getElementsByClassName("reset-button");
for (const button of resetButtons) {
  button.addEventListener("click", resetLocalStorage);
}

// reinitialisate localStorage
function resetLocalStorage() {
    const buttonType = this.innerText.toLowerCase(); // Récupérer le type de bouton ("conversion" ou "weather")
    localStorage.removeItem(`${buttonType}History`);
    alert("Local storage has been reset.");
    location.reload();
  }
  
// reinitialisate localStorage of météo
function resetWeatherLocalStorage() {
    setTimeout(() => {
      localStorage.removeItem("weatherHistory");
      alert("Local storage for weather has been reset.");
    }, 0);
  }

const resetWeatherButton = document.getElementById("reset-weather-button");
resetWeatherButton.addEventListener("click", resetWeatherLocalStorage);