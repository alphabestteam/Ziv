function isSufficientFuel(distance, literPerKM, fuelLeft) {
    /*
    The function receives the distance, the amount of liters per KM, and the amount of fuel left
    The function returns true if there it enough fuel, otherwise false
    */
        return distance * literPerKM <= fuelLeft
    }
    console.log(isSufficientFuel(10, 10, 200));