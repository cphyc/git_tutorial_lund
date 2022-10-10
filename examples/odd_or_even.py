"""A sophisticated example of a Python script that reads a number in and returns whether it is even or odd."""

def read_int_from_stdin():
    """Read one number from stdin and return it as an integer.
    
    Returns
    -------
        int: The number read from stdin.

    Help
    ----
    https://docs.python.org/3/library/funxctions.html#input
    """
    # At the moment we fake the implementation and return a random number between
    # 0 and 100.
    import random
    return random.randint(0, 100)

def check_number_is_int(number):
    """Check if a number is an integer.
    
    Parameters
    ----------
    number: int
        The number to check.
    
    Returns
    -------
    bool
        True if the number is an int, False otherwise.

    Help
    ----
    https://docs.python.org/3/library/functions.html#isinstance
    """
    # At the moment, we fake the implementation and always return True.
    return True

def print_is_odd_or_even(number):
    """Prints "odd" if a number is odd or even otherwise.
    
    Parameters
    ----------
    number: int
        The number to check.

    Help
    ----
    https://docs.python.org/3/library/functions.html#divmod
    """
    # At the moment, we always print a dummy string.
    print("I haven't been taught how to distinguish between odd and even numbers yet.")
    print("Come back later!")

def main():
    number = read_int_from_stdin()
    assert check_number_is_int(number)
    print_is_odd_or_even(number)


if __name__ == "__main__":
    main()