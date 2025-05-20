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
        """Initialize the square object with size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """get area of square."""

        return self.__size * self.__size
