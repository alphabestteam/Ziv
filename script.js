const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

const toggleBob = function() {
  if (button.getAttribute('button-tracker') === 'hidden' || !button.getAttribute('button-tracker')) {
    //This is the initial state of the button where the image is hidden
     bobGif.style.display = 'none';
     button.textContent = 'Show me Bob';
     button.setAttribute('button-tracker', 'visible'); 
  } else {
    //This is once the button ic clicked and the image is revealed
    bobGif.style.display = 'block';
    button.textContent = 'Hide Bob';
    button.setAttribute('button-tracker', 'hidden');
  }
};

//My custom attribute tracks the state of the button, and whether it keeps the image hidden or visible
//I added this attribute in the HTML but the code will also work without this addition
button.setAttribute('button-tracker', 'hidden'); 
button.onclick = toggleBob;
toggleBob(); 