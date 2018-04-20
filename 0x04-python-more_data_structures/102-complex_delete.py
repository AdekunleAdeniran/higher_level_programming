#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for key1, val in new.items():
        if val == value:
            del a_dictionary[key1]
    return a_dictionary
