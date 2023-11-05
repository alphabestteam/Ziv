
/*
The at() method is equivalent to the bracket notation and both return the element at a specified index.
However, there is a key difference between the two.
The at() method cannot accept a negative or out-of-bounds index.
For example, arr[-1] will return the last item in the array.
The arr.at(-1) method will return undefined.
*/
function charArray(inputChar, arrayLength) {
    const newArray = Array.from({ length: arrayLength }, () => inputChar);
    return newArray;
}

function removeNElements(inputArray, n) {
    if (n >= 0 && n <= inputArray.length) {
        return inputArray.slice(0, inputArray.length - n);
    }
    else {
        console.log("Invalid value of n");
        return inputArray;
    }
}

function addElement(inputArray, inputNumber) {
    inputArray.unshift(inputNumber);
    return inputArray;
}

function arrayConcat(firstArr, secondArr) {
    return firstArr.concat(secondArr);
}

function convertArrayUppercase(inputArray) {
    return inputArray.map(function(currentStr) {
        return currentStr.toUpperCase();
    }
    );
}

function doubleDigitsFilter(inputArray) {
    return inputArray.filter(function(inputArray) {
      return inputArray >= 10 && inputArray < 100  && Number.isInteger(inputArray);
    }
    );
  }

function elementInArray(inputArray, inputElement) {
    return inputArray.includes(inputElement);
}

function elementGreaterThanTen(inputArray) {
    return inputArray.find((element) => element > 10);
  }
  

function isThereSuchNumber(inputArray){
    return elementGreaterThanTen(inputArray) >= 0
}

/*
The sort() function sorts values as strings and not numerically.
When numbers are sorted as strings, they will be sorted based on the first digit, then the second, and so on.
For example, 33 is bigger than 122, since the 3 and 1 are compared first. 
Because of this, sort() doesn't sort numeric arrays properly.
*/

function sortNumericArray(inputArray){
    //I'm using the compare function to sort properly
    inputArray.sort(function(a, b){return a - b});
    return inputArray
}

function splitWithAsterisk(inputArray) {
    const sortedArray = sortNumericArray(inputArray)
    return sortedArray.join('**');
  }

function sortAlphabeticArray(inputArray){
    return inputArray.sort();
}

function lesserThanNumber(inputNumber, greaterNumber) {
    //Inner function- checks if all the numbers in the array are lesser than the other
  return inputNumber < greaterNumber;
}

function arrayLesserThan(inputArray, inputNumber) {
    //Checks if all of the elements in the array are lesser than the target

  return inputArray.every((currentElement) => lesserThanNumber(currentElement, inputNumber));
}

function greaterThanNumber(inputNumber, lesserNumber) {
    //Inner function- checks if one number in the array is greater than the other
    return inputNumber > lesserNumber;
  }
  
  function arrayGreaterThan(inputArray, inputNumber) {
    //Checks if any of the elements in the array are greater than the target
    return inputArray.some((currentElement) => greaterThanNumber(currentElement, inputNumber));
  }