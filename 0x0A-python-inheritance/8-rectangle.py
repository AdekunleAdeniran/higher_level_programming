#!/usr/bin/python3
'''8-base_geometry.py'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''private instantiation of attributes
           validate type with integer_validator
        '''
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height
