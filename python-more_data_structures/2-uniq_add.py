#!/usr/bin/python3
def uniq_add(my_list=[]):
    verif = []
    res = 0
    for i in my_list:
        if i not in verif:
            verif.append(i)
            res += i
    return res
