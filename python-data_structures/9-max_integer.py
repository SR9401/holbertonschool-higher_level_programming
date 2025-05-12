#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        tri = sorted(my_list)
        i = len(my_list) - 1
        val_max = tri[i]
        return val_max
