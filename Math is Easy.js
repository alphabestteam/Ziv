function evalNumbers(firstNumber, secondNumber, operation) {
    /*
    The function receives the distance, the amount of liters per KM, and the amount of fuel left
    The function returns true if there it enough fuel, otherwise false
    */
    if (firstNumber < secondNumber){
        let numberContainer = secondNumber;
        secondNumber = firstNumber;
        firstNumber = numberContainer;
    }
    switch (operation){
        case "ADD":
            return firstNumber + secondNumber;
        case "SUBTRACT":
            return firstNumber - secondNumber;
        case "MULTIPLY":
            return firstNumber * secondNumber;
        case "DIVIDE":
            return firstNumber / secondNumber;
        case "MODULUS":
            return firstNumber % secondNumber;
       default:
        return "Invalid inputs";
        }
}
    console.log(evalNumbers(2, 8,"MODULUS"));