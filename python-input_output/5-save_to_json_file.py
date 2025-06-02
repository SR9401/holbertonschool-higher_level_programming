#!/usr/bin/python3
"""Définit une fonction qui lit le contenu d’un fichier texte"""

import json


def save_to_json_file(my_obj, filename):
    """function that returns an object
    (Python data structure) represented by a JSON string"""
    with open(filename, "w") as f:
        (json.dump(my_obj, f))
