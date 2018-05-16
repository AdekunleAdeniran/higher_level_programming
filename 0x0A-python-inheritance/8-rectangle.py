#!/usr/bin/python3
'''8-base_geometry.py'''


class BaseGeometry:
    '''
    class BaseGeometry
    '''

    def area(self):
        '''
        raise an exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        check value input is correct type
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
