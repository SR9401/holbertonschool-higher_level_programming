#!/usr/bin/python3

def print_list_integer(my_list=[]):
    i = 0
    count = len(my_list) - 1
    while i <= count:
        print("{:d}".format(my_list[i]))
        i += 1
