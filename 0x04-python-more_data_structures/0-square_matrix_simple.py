#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for x in range(len(matrix)):
        tmp_list = []
        for i in matrix[x]:
            tmp_list.append(i**2)
        result_matrix.append(tmp_list)
    return (result_matrix)
