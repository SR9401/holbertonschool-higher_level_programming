#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = {}
    for key in a_dictionary:
        n_dictionary[key] = a_dictionary[key]

    for key in n_dictionary:
        n_dictionary[key] = n_dictionary[key] * 2
    return n_dictionary
