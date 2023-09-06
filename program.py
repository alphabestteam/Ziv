#The range is 1-100, so the loop must end at 101
END_OF_RANGE = 101

def factorial_calc(input_number: int) -> int:
    """
    The function receives a number
    The function calculates and returns its factorial
    """
    final_factorial = 1
    for current_number in range(1, (input_number + 1)):
        final_factorial = final_factorial * current_number
    return final_factorial

final_sum = 0
for current_number in range(1, END_OF_RANGE):
    final_sum += current_number
print(final_sum)

input_number = int(input("Enter a number: "))
print(factorial_calc(input_number))