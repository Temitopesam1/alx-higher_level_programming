#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in matrix:
       matrix2.append(list(map(lambda a : pow(a, 2), i)))
    return matrix2

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
