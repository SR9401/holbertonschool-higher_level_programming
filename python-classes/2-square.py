#!/usr/bin/python3

"""
This module provides classes and functions to manage users and greet them.
It demonstrates basic concepts of object-oriented programming in Python.
"""


class Square:
    """This class represents a square.

    It defines a square by its size, with validation to ensure the size
    is a non-negative integer.
    """

    def __init__(self, size=0):
        """Initialize the square object with size.

        Args:
            size (int): The size of one side of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self._Square__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
