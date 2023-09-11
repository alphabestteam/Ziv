from person import Person


def print_numbers(first_number, second_number) -> None:
    """
    The function receives two numbers and prints the to the screen
    If they are not numbers, an exception is raised
    In any case, "finished running" will be printed
    """
    try:
        print(
            f"The first number is {first_number / 1} and the second number is {second_number / 1}"
        )
    except TypeError as message:
        print(f"One of the inputs is not actually a number: {message}")
    finally:
        print("Finished running")


def squared_list(n: int) -> list:
    """
    The function receives n (integer)
    The function returns a list of all the number between 1 and n, squared
    """
    return [current_number**2 for current_number in range(1, n + 1)]


def person_list(n: int) -> list:
    """
    The function receives the integer n
    Creates and returns a list of n Person objects
    """
    people_list = []
    for _ in range(n):
        people_list.append(Person())
    return people_list


def legal_people_list(n: int) -> list:
    """
    The function receive the number n
    Creates and returns a list of n Person objects, using the person_list() functions
    And returns a new, filtered list only with legal people(eighteen or older)
    """
    original_list = person_list(n)
    return [
        current_person for current_person in original_list if current_person.age >= 18
    ]


print_numbers(1, "3")
squared_list(10)
legal_people_list(10)
