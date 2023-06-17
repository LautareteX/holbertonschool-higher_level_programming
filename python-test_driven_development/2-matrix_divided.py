#!/usr/bin/python3
"""
Div matrix func
"""


def matrix_divided(matrix, div):

    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for iterator in matrix:
        for m_element in iterator:
            if type(m_element) != int and type(m_element) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []

    for i in matrix:
        div_i = []
        for j in i:
            div_element = round(j / div, 2)
            div_i.append(div_element)
        divided_matrix.append(div_i)
    return divided_matrix
