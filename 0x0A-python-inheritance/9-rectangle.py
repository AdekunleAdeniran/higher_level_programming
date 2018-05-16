#!/usr/bin/python3
'''9-base_geometry.py'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle inherits from BaseGeometry'''

    def __init__(self, width=0, height=0):
        '''private instantiation of attributes
           validate type with integer_validator
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''informal representation of a Rectangle'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        '''formal representation of a Rectangle'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
