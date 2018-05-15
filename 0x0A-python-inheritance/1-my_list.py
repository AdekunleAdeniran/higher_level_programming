#!/usr/bin/python3
'''
Python class to inherit from list class
'''


class MyList(list):
    '''
    Class inheritance
    '''

    def print_sorted(self):
        print(sorted(self))
