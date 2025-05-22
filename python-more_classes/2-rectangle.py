#!/usr/bin/python3

"""
This module defines a Recatangle class as part of an object-oriented
programming
example. It can be extended later to include attributes and methods relevant
to rectangle.
"""


class Rectangle:

    """This class represents a rectangle.

    Currently, it serves as a placeholder and does not implement
    any attributes
    or methods.
    """

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle height * width"""
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter = height * 2 + width * 2"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
