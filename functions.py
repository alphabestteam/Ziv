import math, random

def adding_numbers(first_number = 0, second_number = 0):
    """"
    The function receives two numbers and returns their sum
    If no value is passed the default value is zero
    """
    return first_number + second_number


def personalized_greeting(input_name: str) -> None:
    """
    The function receives a name
    The function uses string formatting to print a greeting with the name
    """
    print(f"Hello {input_name}! Greet to meet you")

def quadratic_formula(aNum: int, bNum: int, cNum: int) -> None:
    """
    The function receives three numbers
    If possible, the function performs the quadratic formula on them and prints the two solutions
    Otherwise, if isn't possible, the function prints a message that says so
    """
    try:
        print(f"The first number is {(-bNum + math.sqrt((bNum**2) - (4 * aNum * cNum))) / (2 * aNum)}")
        print(f"The second number is {(-bNum - math.sqrt((bNum**2) - (4 * aNum * cNum))) / (2 * aNum)}")
    except:
        print(
            "Value error. It is impossible to use the quadratic formula on these three numbers"
        )


def generate_random(first_number, second_number):
    """
    The function receives two numbers
    The function generates and prints two numbers in that range, one int and one float
    If the second number is larger than the first, the function switches them
    """
    if second_number < first_number: #Incase the range isn't correct
        container_number = first_number
        first_number = second_number
        second_number = container_number                          
    print(f"The random integer is {random.randint(first_number, second_number)}")
    print(f"The random integer is { random.uniform(first_number, second_number)}")


print(f"The result of the addition is {adding_numbers(3, 5)}")
personalized_greeting("Patrick Starr")
quadratic_formula(3, 10, 8)
generate_random(10, 5)


