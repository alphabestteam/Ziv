document.addEventListener('DOMContentLoaded', function() {
    const mainHeading = document.getElementById("main-heading");
    console.log('ID: ' + mainHeading.id);
    console.log('Class Name: ' + mainHeading.className);
    console.log('Class List:', mainHeading.classList);

    const dataStandard = mainHeading.dataset.standard;
    const dataNonStandard = mainHeading.getAttribute('nonStandard');
    console.log('Data Standard:', dataStandard);
    console.log('Data Non-Standard:', dataNonStandard);

    mainHeading.classList.add("bg-lightcyan", "border");

    console.log('Text Content:', mainHeading.textContent);
    console.log('Text Content (without whitespace):', mainHeading.textContent.replace(/\s/g, ''));
    mainHeading.textContent = "Hello there Pearl!";

    //I couldn't find the span tag the instructions were referring to so I create one myself
    const spanElement = document.createElement('span');
    spanElement.textContent = "It's me, SpongeBob!";
    mainHeading.appendChild(spanElement);
    console.log("Heading element: ", mainHeading);

    const cloned = mainHeading.cloneNode(true);
    console.log("Cloned element:", cloned);

    //I also couldn't find the h2 tag the instructions were referring to so I create one myself
    const subheading = document.createElement('h2');
    subheading.textContent = "Jellyfish hunting is the best";
    document.body.appendChild(subheading)

    const loremString ="Lorem ipsum dolor sit amet consectetur adipisicing elit. \
    Labore eum, earum deserunt numquam quis explicabo. Delectus id, cum voluptate \
    dicta aperiam sunt voluptatum quis eaquealiquam distinctio reiciendis iste minima?"
    const loremArray = loremString.split(' ');

    function randomArrayElement(inputArray) {
        const randomIndex = Math.floor(Math.random() * inputArray.length);
        return inputArray[randomIndex];
    }

    const randomWords = document.getElementById("random-words");

    function getRandomColor(){
        //I had to define a function that generates ransom colors since one doesn't exist
        return "#" + Math.floor(Math.random() * 16777215).toString(16);
    }

    loremArray.forEach((element, index) => {
        const span = document.createElement("span");
        const style = "background-color: "+ getRandomColor();
        span.setAttribute("style", style);
        span.textContent = element +" ";
        span.className = "random-words";
        randomWords.appendChild(span);
    });

});
