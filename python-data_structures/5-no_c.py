#!/usr/bin/python3
def no_c(my_string):

    char = my_string.split("c")
    n_string = "".join(char)
    nchar = n_string.split("C")
    nn_string = "".join(nchar)
    return nn_string
