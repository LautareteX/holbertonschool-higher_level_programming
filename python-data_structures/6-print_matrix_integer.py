#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for value in matrix:
        for i, j in enumerate(value, start=1):
            if i != 1:
                print("{}".format(" "), end="")
            print("{:d}".format(j), end="")
        print()
