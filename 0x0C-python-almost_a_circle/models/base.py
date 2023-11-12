#!/usr/bin/python3
"""THE BASE MODULE
this module is the base of other modules
"""
import json


class Base():
    """the base class definition
        attributes:
        id: the id of the instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a js object from a list of dicts
            Args:
                list_dictionaries: the list of dicts
        """
        if (list_dictionaries is None):
            return ([])
        elif (len(list_dictionaries) == 0):
            return ([])
        js = json.dumps(list_dictionaries)
        return (js)

    def save_to_file(cls, list_objs):
        """save the json list to a file
           args:
                cls:
                list_objs:
        """
        js_ = Base.to_json_string(list_objs)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """from a text json to a dictionary
           Args:
               json_string: the txt json represantation
        """
        if (json_string is None):
            return ([])
        elif (len(json_string) == 0 or json_string == ""):
            return ([])
        dict_ = json.loads(json_string)
        return (dict_)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary
        of attributes
        Args:
            **dictionary: a dict of attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Loads an object from a file
        and return a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
