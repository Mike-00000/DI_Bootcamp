
// Exercise 2 : Move The Box

function myMove() {
    var animate = document.getElementById("animate");
    var container = document.getElementById("container");
    var width = container.offsetWidth;
    var position = 0;
    var interval = setInterval(function() {
      position++;
      animate.style.left = position + "px";
      if (position >= width - animate.offsetWidth) {
        clearInterval(interval);
      }
    }, 1);
  }
  