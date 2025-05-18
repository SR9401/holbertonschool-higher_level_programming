#!/usr/bin/python3
"""
This module defines a function that prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            j += 1
        print()
        i += 1
