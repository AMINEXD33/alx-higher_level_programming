#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    result_list = []
    flag = 1
    for x in range(list_length):
        try:
            if (type(my_list_1[x]) is int or type(my_list_1[x]) is float):
                if (type(my_list_2[x]) is int or type(my_list_2[x]) is float):
                    try:
                        result = my_list_1[x] / my_list_2[x]
                    except ZeroDivisionError:
                        print("division by 0")
                    finally:
                        result_list.append(result)
                        result = 0
                        flag = 1
                else:
                    flag = 0
            else:
                flag = 0
            if (flag == 0):
                print("wrong type")
                result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
    return result_list
