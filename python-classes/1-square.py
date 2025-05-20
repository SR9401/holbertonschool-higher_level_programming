#!/usr/bin/python3

"""
This module defines a Square class as part of an object-oriented programming
example. It can be extended later to include attributes and methods relevant
to geometric squares.
"""


class Square:
    """This class defines a square by its size."""

    def __init__(self, size):
        """Initialize the square object with size.

        Args:
            size (int): The size of one side of the square.
        """
        self._Square__size = size
