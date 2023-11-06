#!/usr/bin/python3
"""Geometry module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Geometry class"""
    def __init__(self, width, height):
        """construc"""
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.width = width
        self.height = height