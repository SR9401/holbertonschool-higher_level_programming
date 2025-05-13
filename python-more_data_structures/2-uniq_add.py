#!/usr/bin/python3
def uniq_add(my_list=[]):
    verif = []
    i = 0
    res = 0
    verif.append(my_list[0])
    res += my_list[0]
    while i != len(my_list):  
        v = 0
        while v != len(verif):
            if verif[v] == my_list[i]:
                i += 1
            v += 1
        verif.append(my_list[i])
        res += my_list[i]
        i += 1
    return res
