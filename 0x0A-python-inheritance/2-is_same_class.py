#!/usr/bin/python3
'''
Python function to check instance of specified object
'''


def is_same_class(obj, a_class):
    '''
    check if instance is same
    '''
    return issubclass(a_class, type(obj))
