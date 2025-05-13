#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    new_matrix = []
    while i < (len(matrix)):
        j = 0
        res = []
        while j < (len(matrix[i])):
            val = matrix[i][j]
            res.append(val * val)
            j += 1
        new_matrix.append(res)
        i += 1
    return new_matrix
