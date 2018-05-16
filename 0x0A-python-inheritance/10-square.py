#!/usr/bin/python3
'''9-base_geometry.py'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.size ** 2
