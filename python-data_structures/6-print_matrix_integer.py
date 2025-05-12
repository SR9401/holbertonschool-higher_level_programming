#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    if len(matrix) - 1 == 0:
        print("")
    else:
        while i < len(matrix):

            print("{:d} {:d} {:d}".format(*matrix[i]))
            i += 1
