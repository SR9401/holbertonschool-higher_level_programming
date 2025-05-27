#!/usr/bin/python3
"""This module defines the MyList class that extends the built-in list
with a method to print its elements sorted."""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is exactly
    an instance of the specified class ; otherwise False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
