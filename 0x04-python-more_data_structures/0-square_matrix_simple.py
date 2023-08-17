#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result = []
    matrix = [row[:] for row in matrix]

    for row in matrix:
        sq = []
        for element in row:
            if isinstance(element, int):
                sq.append(element ** 2)
            else:
                sq.append(element)
        result.append(sq)
    return result
    return matrix
