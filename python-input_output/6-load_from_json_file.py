#!/usr/bin/python3
"""Définit une fonction qui lit le contenu d’un fichier texte"""

import json


def load_from_json_file(filename):
    """function that returns an object
    (Python data structure) represented by a JSON string"""
    with open(filename, "r") as f:
        return (json.load(f))
