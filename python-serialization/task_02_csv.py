#!/usr/bin/python3

import csv
import json

class DictReader:


    def convert_csv_to_json(file):
        with open('input.csv', mode='r', newline='', encoding='utf-8') as csvfile:
            data = list(csv.DictReader(csvfile))

            with open('output.json', mode='w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)