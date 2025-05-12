#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    n_list = list.copy(my_list)
    while i <= len(my_list) - 1:
        if (my_list[i] % 2) == 0:
            n_list[i] = True
        else:
            n_list[i] = False
        i += 1
    return n_list
