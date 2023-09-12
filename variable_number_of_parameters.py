def word_length(*args) -> None:
    """
    The function receives an unlimited number of words
    The functions prints the length of each word
    """
    for current_word in args:
        print(f"{current_word}: {len(current_word)}")


def total_age(**kwargs) -> None:
    """
    The function receives an unlimited number of keyword arguments of ages
    The function prints each age name and value
    The function also sums up all the ages and prints the result
    """
    ages_sum = 0
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        ages_sum += value
    print(f"Sum of the ages: {ages_sum}")


def main():
    word_length("Course", "Computer", "Frosted flakes", "Expensive")
    total_age(age1=10, age2=20, age3=30)


if __name__ == "__main__":
    main()
