function createCounter() {
    const button = document.getElementById("my-button");
    const buttonCounter = document.getElementById("counter-display");
    let buttonClicksNumber = 0;
  
    function closure() {
        //Inner function that's triggered when the button is clicked
        buttonClicksNumber++;
        buttonCounter.textContent = buttonClicksNumber;
    }
  
    button.addEventListener("click", closure);
  }
  
  createCounter(); 
  