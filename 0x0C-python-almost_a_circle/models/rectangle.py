#!/usr/bin/python3
"""Class Rectangle which inherits from base"""


from models.base import Base


class Rectangle(Base):
    ''''Rectangle methods and fields'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiation of attributes'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update(self, *args, **kwargs):
        '''Set up args for rectangle'''
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, values in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, values)

    def area(self):
        '''Method that returns the area of class Rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Method for printing  Rectangle to stdout'''
        print('\n' * self.y, end="")
        for h in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        '''Method that returns string representation of rectangle '''
        a, d, e = self.id, self.width, self.height
        b, c = self.x, self.y
        return("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    @property
    def width(self):
        """set the property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """set the property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        '''set the height attribute'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """set the property of x"""
        return self.__x

    @x.setter
    def x(self, value):
        '''set the x positional attribute'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """set the property of y"""
        return self.__y

    @y.setter
    def y(self, value):
        '''set the y positional attribute'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def to_dictionary(self):
        '''Method that returns dictionary representaton of rectangle'''
        dic = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return dic
