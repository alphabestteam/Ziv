import time


def timer(input_function):
    """
    Decorates running function
    prints inner function's runtime
    """

    def wrapper(*args):
        starting_time = time.time()
        function_result = input_function(*args)
        ending_time = time.time()
        print(f"Function running time: {ending_time - starting_time}")
        return function_result

    return wrapper


@timer
def add_numbers(x_number, y_number):
    """
    The function receives two numbers and prints their sum
    """
    return x_number + y_number


print(add_numbers(2, 4))
