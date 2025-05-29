#!/usr/bin/env python3
"""Abstract Base Classes (ABCs)"""

from abc import ABC, abstractmethod
from math import *


class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with a radius"""
        self.radius = radius

    def perimeter(self):
        """Return the perimeter of the circle (2 * π * radius)"""
        return 2 * pi * self.radius

    def area(self):
        """Return the area of the circle (π * radius^2)"""
        return pi * self.radius ** 2


# Define a concrete subclass Rectangle that inherits from Shape
class Rectangle(Shape):
    def __init__(self, height, width):
        """Initialize the rectangle with height and width"""
        self.width = width
        self.height = height

    def perimeter(self):
        """Return the perimeter of the rectangle (2 * (width + height))"""
        return 2 * (self.width + self.height)

    def area(self):
        """Return the area of the rectangle (width * height)"""
        return self.width * self.height


def shape_info(shape):
    """
    Print the area and perimeter of any shape object
    that implements the area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
