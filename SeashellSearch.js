function findSeashellsIndices(arr, target) {
    let secondNumber = 0;
    for (let firstNumber = 0; firstNumber < arr.length; firstNumber++) {
        secondNumber = arr.indexOf(target - arr[firstNumber]);
        if(secondNumber >= 0){        
            return [firstNumber, secondNumber];
        }
    }
    return [];
}

const result = findSeashellsIndices([5, 10, 15, 21, 25], 30);
console.log(result);