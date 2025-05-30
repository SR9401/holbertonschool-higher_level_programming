#!/usr/bin/python3
"""This module defines the MyList class that extends the built-in list
with a method to print its elements sorted."""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False"""
    return (isinstance(obj, a_class)) and type(obj) is not a_class
