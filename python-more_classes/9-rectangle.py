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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """function to print rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        form = []
        i = 0
        while i != self.__height:
            form.append(str(self.print_symbol) * self.__width)
            i += 1
        return "\n".join(form)

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance by using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message Bye rectangle...
        when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
