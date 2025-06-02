#!/usr/bin/python3
"""Définit une fonction qui lit le contenu d’un fichier texte"""

import json


def from_json_string(my_str):
    """function that returns an object
    (Python data structure) represented by a JSON string"""
    return (json.loads(my_str))
