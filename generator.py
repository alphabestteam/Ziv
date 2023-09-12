def N_numbers(N: int) -> int:
    """
    The function receives integer N 
    The function yields N numbers of the given sequence
    """
    yield 1
    first_number, second_number = 1, 2
    for _ in range(N):
        first_number, second_number = second_number, first_number * second_number
        yield first_number



for current_number in N_numbers(10):
    print(current_number)