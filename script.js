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
const INTERVAL_MS = 1000;

function startTimer() {
    timeRun = setInterval(function () {
        timeThatPassed++;
        showTimerToPlayer();
    }, INTERVAL_MS);
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

function loadTableAfterRefresh() {
    const scoreHistory = localStorage.getItem("scores");
    if (scoreHistory) {//In case there are no scores yet because this is the first game
        const scoresResult = JSON.parse(scoreHistory);
        scoresResult.forEach((score) => {
            updateScoreboard(score.words, score.time, score.wpm, score.accuracy);
        });
    }
}


function startGame() {
    // Load saved scores from localStorage when the game starts
    loadTableAfterRefresh();

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

    // Button is clicked- starts the game
    startButton.addEventListener("click", triggeredButton);

    // Enter- starts the game
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
    for (let index = 0; index < strA.length; index++) {
        if (strA[index] == strB[index]) {
            matchingChars++;
        }
    }
    return (matchingChars / strB.length) * 100
}

function scoreCalculator(accuracy, wordsPerMinute) {
    return accuracy * (wordsPerMinute / 10)

}


function updateScoreboard(words, time, wpm, accuracy) {
    const scoreboard = document.getElementById("scoreboard");
    const newScore = scoreCalculator(accuracy, wpm);


    // Create a new row for this round of the game
    const newGameRecord = document.createElement("tr");
    newGameRecord.innerHTML = `
      <td></td>
      <td>${words}</td>
      <td>${time}</td>
      <td>${wpm.toFixed(2)}</td>
      <td>${accuracy.toFixed(2)}%</td>
      <td>${newScore.toFixed(2)}</td>
    `;

    // Add the new row to the scoreboard
    scoreboard.appendChild(newGameRecord);

    // Sort by ranking
    const rows = scoreboard.querySelectorAll("tr");
    const scores = Array.from(rows).map((row, index) => ({
        row,
        score: parseFloat(row.querySelector("td:last-child").textContent),
    }));
    scores.sort((a, b) => b.score - a.score);

    scores.forEach((score, index) => {
        score.row.querySelector("td:first-child").textContent = index + 1;
    });

    // Remove the old rows from the table and add the sorted ones
    scoreboard.innerHTML = "";
    scores.forEach((score) => scoreboard.appendChild(score.row));

    // Save the scores in localStorage as JSON
    const scoresResult = scores.map((score) => ({
        words: parseFloat(score.row.querySelector("td:nth-child(2)").textContent),
        time: score.row.querySelector("td:nth-child(3)").textContent,
        wpm: parseFloat(score.row.querySelector("td:nth-child(4)").textContent),
        accuracy: parseFloat(score.row.querySelector("td:nth-child(5)").textContent),
        score: parseFloat(score.row.querySelector("td:last-child").textContent),
    }));

    localStorage.setItem("scores", JSON.stringify(scoresResult));
}

function endGame() {
    const gameTime = stopTimer();
    activeGameFlag = false;
    const inputAnswer = document.getElementById("input");
    const outputQuote = document.getElementById("quote").textContent;
    const wordCount = outputQuote.split(" ").length;
    const accuracy = countMatchingChars(inputAnswer.value, outputQuote);
    const wpm = (wordCount / gameTime) * 60;

    const rating = document.getElementById("result");
    rating.textContent = `You typed ${wordCount} words in ${gameTime} seconds. Your speed is ${wpm.toFixed(2)} words per minute with ${accuracy.toFixed(2)}% accuracy`;

    //Clear input bar for next round
    inputAnswer.value = "";

    // Reset the background colors of characters in the quote
    const quoteChars = document.getElementById("quote").querySelectorAll("span");
    for (let i = 0; i < quoteChars.length; i++) {
        quoteChars[i].style.backgroundColor = "transparent";
    }

    // Update the table with the game statistics
    updateScoreboard(wordCount, gameTime, wpm, accuracy);
}
startGame();