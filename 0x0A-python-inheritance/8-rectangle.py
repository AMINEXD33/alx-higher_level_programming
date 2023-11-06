#!/usr/bin/python3
"""Geometry module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry(BaseGeometry):
    """Geometry class"""
    def __init__(self, width, height):
        """construc"""
        integer_validator(self, 'width', width)
        integer_validator(self, 'height', height)
        self.width = width
        self.height = height