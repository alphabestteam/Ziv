#The range is 1-100, so the loop must end at 101

def is_prime(currentNum: int, divider=2) -> bool:
    """
    The function receives a number and checks if if it's prime through recursion
    The function returns true if it is, otherwise false
    """

    if currentNum <= 2:
        return True if (currentNum == 2 or currentNum == 1) else False
    if currentNum % divider == 0:
        return False
    if divider * divider > currentNum:
        return True
    return is_prime(currentNum, divider + 1)


def prints_primes(number_list: list) -> None:
    """
    Th function is a wrapper for the isPrime function
    the function receives a number
    The function prints all prime numbers up until the number, which is included
    """

    for currentNum in number_list:
        if is_prime(currentNum):
            print(f"{currentNum}")

END_OF_RANGE = 101 
final_sum = 0
for current_number in range(1, END_OF_RANGE):
    final_sum += current_number
print(final_sum)

prints_primes([5, 6, 7, 14, 152, 60693])