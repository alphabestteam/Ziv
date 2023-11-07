const quotes = [
    "I'm ready, I'm ready, I'm ready! -SpongeBob SquarePants",
    "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! -SpongeBob SquarePants",
    "I'm not just ready, I'm ready Freddy! -SpongeBob SquarePants",
    "Remember, licking doorknobs is illegal on other planets. -SpongeBob SquarePants",
    "The inner machinations of my mind are an enigma. -Patrick Star",
    "I can't hear you, it's too dark in here! -Patrick Star",
    "I'm ugly and I'm proud! -SpongeBob SquarePants",
    "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. -Squidward Tentacles",
    "Once there was an ugly barnacle. He was so ugly that everyone died. The end. -Patrick Star",
    "Is mayonnaise an instrument? -Patrick Star",
    "Can you give SpongeBob his brain back? -Patrick Star",
    "I guess hibernation is the opposite of beauty sleep. -Squidward Tentacles",
    "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! -SpongeBob SquarePants",
    "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! -SpongeBob SquarePants",
    "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. -Bubble Bass",
    "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
    "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
    "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. -Squidward: What's that? -SpongeBob: Outdoors.",
    "SpongeBob: Can I be excused for the rest of my life?",
    "SpongeBob: I'm not just ready, I'm ready Freddy!",
    "SpongeBob: You don't need a license to drive a sandwich.",
    "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
    "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
    "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
    "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end."
];

let timeRun;
let timeThatPassed = 0;
let activeGameFlag = false;

function startTimer() {
    timeRun = setInterval(function () {
        timeThatPassed++;
        showTimerToPlayer();
    }, 1000);
}

function stopTimer() {
    clearInterval(timeRun);
    showTimerToPlayer();
    return timeThatPassed;
}

function showTimerToPlayer() {
    const gameTime = document.getElementById("timer");
    gameTime.textContent = `${timeThatPassed} seconds`;
}

function getRandomQuote() {
    return quotes[Math.floor(Math.random() * quotes.length)];
}

function startGame() {
    const presentedQuote = document.getElementById("quote");
    const inputElement = document.getElementById("input");
    const startButton = document.getElementById("start-btn");

    function triggeredButton() {
        if (!activeGameFlag) {
            presentedQuote.textContent = getRandomQuote();
            timeThatPassed = 0;
            startTimer();
            activeGameFlag = true;
        }
    }

    // Button is clicked- starts game
    startButton.addEventListener("click", triggeredButton);

    // Enter- starts game
    document.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            if (activeGameFlag) {
                endGame();
            } else {
                triggeredButton();
            }
        }
    });

    showTimerToPlayer();
    inputElement.addEventListener("input", checkInput);
}

function checkInput() {
    if (!activeGameFlag) return;

    const inputElement = document.getElementById("input");
    const quoteElement = document.getElementById("quote");
    const inputContent = inputElement.value;
    const quoteContent = quoteElement.textContent;
    quoteElement.innerHTML = "";

    for (let i = 0; i < quoteContent.length; i++) {
        const inputChar = inputContent[i];
        const quoteChar = quoteContent[i];

        const markedAnswer = document.createElement("span");
        markedAnswer.textContent = quoteChar;

        if (inputChar === quoteChar) {
            markedAnswer.style.backgroundColor = "green"; 
        } else if (inputChar) {
            markedAnswer.style.backgroundColor = "red"; 
        } else {
            //This is when the input answer isn't the full one, so the rest of the quote is transparent
            markedAnswer.style.backgroundColor = "transparent";
        }

        quoteElement.appendChild(markedAnswer);
    }

    // Checks if the answer is done (regardless of mistakes)
    if (inputContent.length == quoteContent.length) {
        endGame();
    }
}

function countMatchingChars(strA, strB) {
    let matchingChars = 0;
    for(let index = 0; index < strA.length; index++){
        if (strA[index] == strB[index]){
            matchingChars ++;        }
    }
    return (matchingChars / strB.length) * 100
}


function endGame() {
    const gameTime = stopTimer();
    activeGameFlag = false;
    const inputAnswer = document.getElementById("input");
    const outputQuote = document.getElementById("quote").textContent;
    const wordCount = outputQuote.split(" ");
    const rating = document.getElementById("result");
    const accuracy = countMatchingChars(inputAnswer.value, outputQuote);

    rating.textContent = `You typed ${wordCount.length} words\n in ${gameTime} seconds\n\
    Your speed is ${((wordCount.length / gameTime) * 60
    ).toFixed(2)} words per minute\n with ${accuracy.toFixed(2)}% accuracy`;

    inputAnswer.value = "";
    // Reset the background colors of characters in the quote
    const quoteChars = document.getElementById("quote").querySelectorAll("markedAnswer");
    for (let i = 0; i < quoteChars.length; i++) {
        quoteChars[i].style.backgroundColor = "transparent";
    }
}

startGame();