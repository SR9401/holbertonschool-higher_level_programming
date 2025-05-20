#!/usr/bin/python3
"""
This module provides classes and functions to manage users and greet them.
It demonstrates basic concepts of object-oriented programming in Python.
"""
class Square:
    '''this class represent a square '''
    def __init__(self, size=0):
        self._Square__size = size
        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
