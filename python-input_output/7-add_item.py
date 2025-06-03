#!/usr/bin/python3
"""Script qui ajoute tous les arguments à une liste Python,
puis les sauvegarde dans un fichier JSON.
"""

import sys

# Importation des fonctions demandées depuis les modules 5 et 6
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Nom du fichier où la liste sera sauvegardée
filename = "add_item.json"

# Récupération des arguments passés en ligne de commande (sans le nom du script)
args = sys.argv[1:]

# Tentative de chargement du contenu existant dans le fichier
try:
    existing_data = load_from_json_file(filename)
except Exception:
    # Si le fichier n'existe pas encore, on commence avec une liste vide
    existing_data = []

# Ajout des nouveaux arguments à la liste existante
existing_data.extend(args)

# Sauvegarde de la liste complète dans le fichier JSON
save_to_json_file(existing_data, filename)
