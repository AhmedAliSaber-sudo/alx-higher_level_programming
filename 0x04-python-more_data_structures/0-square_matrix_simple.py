#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    return[[element ** 2 in row] for row in matrix]
    return(list(map(lambda x: x ** 2, list)) for list in matrix)
