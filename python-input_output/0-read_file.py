#!/usr/bin/python3
"""Définit une fonction qui lit le contenu d’un fichier texte"""


def read_file(filename=""):
    """Ouvre le fichier en mode lecture ("r"), automatiquement fermé après le bloc"""

    with open(filename, "r") as file:
        contents = file.read()
        print(contents, end="")
