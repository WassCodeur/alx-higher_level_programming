#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character #.
    Args:
        size (int): The size length of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
    returns:
        None

    prints a square with the character #.

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
