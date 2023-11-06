function addEvent() {
    const button = document.getElementById("my-button");
    const buttonCounter = document.getElementById("counter-display");
    let buttonClicksNumber = 0;
    button.addEventListener("click", function() {
        buttonClicksNumber++;
        buttonCounter.textContent = buttonClicksNumber;
    });
 
}
addEvent();