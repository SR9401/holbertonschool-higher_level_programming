#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args = sys.argv[1:]

try:
    exist = load_from_json_file(filename)
except FileNotFoundError:
    exist = []

exist.extend(args)
save_to_json_file(exist, filename)
