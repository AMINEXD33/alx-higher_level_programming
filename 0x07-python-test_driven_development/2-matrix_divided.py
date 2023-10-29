#!/usr/bin/python3
def raise_error1(msg):
    if (msg == 1):
        msg = "matrix must be a matrix"
        msg = msg + " (list of lists) of untegers/floats"
        raise TypeError(msg)
        return
    elif (msg == 2):
        raise TypeError("Each row of the matrix must have the same size")
        return
    elif (msg == 3):
        raise TypeError("div must be a number")
        return
    elif (msg == 4):
        raise ZeroDivisionError("division by zero")
        return


"""
i really dont know what to write here XD
"""


def matrix_divided(matrix, div):
    """divide a matrix by a div
    args:
        matrix: a list of lists, holding only integers or floats
        div: the value to divide on != 0
    Return:
        a new matrix holding the results
    raise:
        TypeError if an element in matrix is not an int or float.
        TypeError if the size of a list inside the matrix is not equal
        to the rest.
        TypeError if the div is not an int or float
        ZeroDivisionError: if div is 0
    """
    # check matrix
    base_len = 0
    flag = True
    for x in range(len(matrix)):
        if (flag):
            base_len = len(matrix[x])
            flag = False
        else:
            if (base_len != len(matrix[x])):
                raise_error1(2)
                return
        for y in range(len(matrix[x])):
            if type(matrix[x][y]) is not int:
                if type(matrix[x][y]) is not float:
                    raise_error1(1)
                    return
                raise_error1(1)
                return
    # check div
    if (type(div) is not int and type(div) is not float):
        raise_error1(3)
        return
    if (div == 0):
        raise_error1(4)
        return
    # divide
    list_ = []
    for x in range(len(matrix)):
        tmp_list = []
        for y in range(len(matrix[x])):
            tmp_list.append(round(matrix[x][y]/div, 2))
        list_.append(tmp_list)

    return list_
