#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for ne in new:
        new[ne] *= 2
    return new
