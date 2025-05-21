#!/usr/bin/python3

"""
This module defines a Square class with a private size attribute.
It demonstrates the use of getter and setter methods through the
@property decorator to ensure encapsulation and data validation.
"""


class Square:
    """This class represents a square.

    It defines a square by its size, with validation to ensure the size
    is a non-negative integer.
    """

    def __init__(self, size=0):
        """Initialize the square object with size."""
        self.size = size  # Use the setter to validate and set the size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
