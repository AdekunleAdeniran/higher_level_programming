#!/usr/bin/python3

'''9-rectangle: Python Funtion that defines Rectangle type'''


class Rectangle:
    '''Defines the Rectangle type'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return""
        else:
            for h in range(self.__height):
                for w in range(self.height - 1):
                    print(str(self.print_symbol) * self.__width)
                return str(self.print_symbol) * self.width

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))

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

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle…")

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
