#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    """class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation
        of a Student instance"""
        if attrs is None:
            return self.__dict__
        dicti = {}

        for attr in attrs:
            if hasattr(self, attr):
                value = getattr(self, attr)
                dicti[attr] = value
        return dicti

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
