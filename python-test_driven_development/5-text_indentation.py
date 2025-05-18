#!/usr/bin/python3
"""
This module defines a function that prints text with two new lines after
each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
