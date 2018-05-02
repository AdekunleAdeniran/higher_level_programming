#!/usr/bin/python3
'''3-square.py: Defines Area that returns the current square area'''


class Square:
    '''Creates  Square type'''

    def __init__(self, size=0):
        '''Initializes Square with size'''
        self.size = size

    @property
    def size(self):
        '''Defines the size of square and returns its value'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Defines the value of size of square and checks if >= 0'''
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size
