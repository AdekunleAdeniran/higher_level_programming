#!/usr/bin/python3

'''
1-rectangle: Python Funtion that defines Rectangle type'''


class Rectangle:
    '''Defines the Rectangle type'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return""
        else:
            for h in range(self.__height):
                for w in range(self.height - 1):
                    print('#' * self.__width)
                return '#' * self.width

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            return (2 * (self.height + self.width))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
