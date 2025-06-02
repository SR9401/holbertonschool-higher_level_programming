#!/usr/bin/python3
"""Définit une fonction qui lit le contenu d’un fichier texte"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""

    with open(filename, "a") as file:
        file.write(text)
        return len(text)
