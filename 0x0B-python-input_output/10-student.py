#!/usr/bin/python3
"""class to json"""


class Student():
    """STUDENT CLASS"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """make dict"""
        #load dict
        dict_ = self.__dict__.copy()
        if type(attrs) is list:
            for x in attrs:
                if (type(x) is not str):
                    return (dict_)

            tmp_ = {}
            for x in range(len(attrs)):
                for i in dict_:
                    if attrs[x] == i:
                        tmp_[i] = dict_[i]
            return (tmp_)
        return (dict_)

