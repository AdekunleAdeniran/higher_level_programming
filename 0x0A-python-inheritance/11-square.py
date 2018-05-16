#!/usr/bin/python3
'''9-base_geometry.py'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator(size, size)
        super().__init__(size, size)
        self.size = size

    def area(self):
        return self.size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.size, self.size)
