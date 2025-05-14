#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    n_list = list.copy(my_list)
    for i in range(len(n_list)):
        n_list[i] = n_list[i] * number
    return n_list
