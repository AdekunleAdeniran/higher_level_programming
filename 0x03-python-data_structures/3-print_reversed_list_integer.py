#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = my_list[::-1]
    for int in n:
        print("{:d}".format(int))
