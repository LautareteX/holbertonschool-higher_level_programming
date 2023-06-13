#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    
    for i in matrix:
        my_matrix.append(list(map(lambda i: i * i, i)))
    return my_matrix
