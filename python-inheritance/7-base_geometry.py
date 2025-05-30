#!/usr/bin/python3
"""This module defines the BaseGeometry class
with a placeholder method for area computation."""


class BaseGeometry:

    """BaseGeometry is a base class for geometric shapes.
    It includes a method placeholder for area computation."""

    def area(self):
        """Raises an Exception to indicate
        that the area method is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validats Value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
