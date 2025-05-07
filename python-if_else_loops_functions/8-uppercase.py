#!/usr/bin/python3

def uppercase(str):
    i = 0
    while i != len(str):
        if ord(str[i]) < 123 and ord(str[i]) > 96:
            maj = chr(ord(str[i]) - 32)
        else:
            maj = str[i]
        print("{}".format(maj), end="")
        i += 1
    print("")
