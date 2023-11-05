const mainString = " Kung Fu Panda is a beloved animated movie about a clumsy,food-loving panda named Po who dreams of becoming a kung fu master.\nPo's dream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release.\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship.\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages"

function arrayOfParagraphs(inputString) {
    return inputString.split('\n');
}

function movieFilmReplacement(inputString) {
    return inputString.replace(/movie/, 'film');
}

function PandaBearReplacement(inputString) {
    //Note that this only replaces 'Panda' and not 'panda'
    return inputString.replace(/Panda/g, 'Bear');
}

function turnToUppercase(inputString) {
    return inputString.toUpperCase()
}

function turnToLowercase(inputString) {
    return inputString.toLowerCase()
}

function firstPoIndex(inputString) {
    return inputString.indexOf("Po");
}

function fromPoToEnd(inputString) {
    const poIndex = inputString.indexOf("Po");
    if (poIndex !== -1) {
        return inputString.slice(poIndex);

    } else {
        return "Po isn't here";
    }
}

function removeWhitespace(inputString) {
    return inputString.replace(/\s/g, "");
}

function fromPoTONewline(inputString) {
    startsAtPo = fromPoToEnd(inputString);
    newlineIndex = startsAtPo.indexOf("\n");
    return startsAtPo.slice(0, newlineIndex)
}

function arrayOfWords(inputString) {
    //This address both newlines and spaces as things that could separate words
    return inputString.split(/\s+/).filter(currentWord => currentWord.trim() !== '');

}

function endsWithAges(inputString) {
    return inputString.endsWith("ages");
}

function addReview(inputString) {
    return inputString + "is one of my favorite movies!";
}