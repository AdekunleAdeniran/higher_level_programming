#!/usr/bin/python3
'''3-square.py: Defines Area that returns the current square area'''


class Square:
    '''Creates  Square type'''

    def __init__(self, size=0):
        '''Initializes Square with size'''
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size
