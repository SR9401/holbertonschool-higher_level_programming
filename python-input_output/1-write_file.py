#!/usr/bin/python3
"""Définit une fonction qui lit le contenu d’un fichier texte"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
    the number of characters written"""

    with open(filename, "w") as file:
        file.write(text)
        return len(text)
