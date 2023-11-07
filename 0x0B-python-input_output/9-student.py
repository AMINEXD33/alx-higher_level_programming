#!/usr/bin/python3
"""class to json"""


class Student():
    """STUDENT CLASS"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """make dict"""
        dict_ = {}
        dict_['first_name'] = self.first_name
        dict_['last_name'] = self.last_name
        dict_['age'] = self.age
        return (dict_)
