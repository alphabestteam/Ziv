function printGreeting(){
    return "Hello World"
}

function printPersonalGreeting(inputName){
    return "Hello " + inputName
}

function squareNumber(inputNumber){
    return inputNumber ** 2
}

function squareArea(width, height){
    return width * height
}

function areaCircumferenceOfCircle(radius) {
    return [2 * radius * Math.PI, Math.PI * (radius ** 2)];
}
  
function countVowels(inputStr) {
    return (inputStr.match(/[aeiouAEIOU]/g) || []).length;
}

function compareArrayLengths(firstArr, secondArr){
    return firstArr.length == secondArr.length
}

function numberToArr(inputNum) {
    return inputNum.toString().split('').map(Number);
}
function truthyFalsyArray(inputArray) {
    return inputArray.map(item => Boolean(item));
}
  