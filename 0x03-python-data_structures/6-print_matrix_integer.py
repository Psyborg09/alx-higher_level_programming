#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) != 0:
            print("{:d} {:d} {:d}".format(row[0], row[1], row[2]))
        else:
            print("".format())
