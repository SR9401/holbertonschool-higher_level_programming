#!/usr/bin/python3
import copy

def multiply_by_2(a_dictionary):
    n_dictionary = copy.deepcopy(a_dictionary)
    for key in n_dictionary:
        n_dictionary[key] = n_dictionary[key] * 2
    return n_dictionary
