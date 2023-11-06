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

    const loremString = "Lorem ipsum dolor sit amet consectetur adipisicing elit. \
    Labore eum, earum deserunt numquam quis explicabo. Delectus id, cum voluptate \
    dicta aperiam sunt voluptatum quis eaquealiquam distinctio reiciendis iste minima?";
    const loremArray = loremString.split(' ');

    function randomArrayElement(inputArray) {
        const randomIndex = Math.floor(Math.random() * inputArray.length);
        return inputArray[randomIndex];
    }

    function getRandomColor(){
        //Randomly generates a color based on the #RRGGBB format
        return "#" + Math.floor(Math.random() * 16777215).toString(16);
    }

    function changeTextColors() {
        //This is the function that the event listener calls once triggered
        const randomWords = document.getElementById("random-words");
        const spans = randomWords.getElementsByClassName("random-words");

        Array.from(spans).forEach((span) => {
            span.style.backgroundColor = getRandomColor();
        });
    }

    //Here I created the button that listens for a click
    const colorChangeButton = document.createElement("button");
    colorChangeButton.textContent = "Change Text Color";
    colorChangeButton.addEventListener("click", changeTextColors);
    document.body.appendChild(colorChangeButton);

    // Create and initialize the 'random-words' section with the initial text content
    const randomWords = document.getElementById("random-words");
    loremArray.forEach((element) => {
        const span = document.createElement("span");
        span.textContent = element + " ";
        span.className = "random-words";
        randomWords.appendChild(span);
    });
});
