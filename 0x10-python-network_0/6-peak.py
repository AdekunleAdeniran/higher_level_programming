#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Python function to find peak number"""
    le = len(list_of_integers)
    if le == 0:
        return
    m = le // 2
    pivot = list_of_integers[m]
    left = list_of_integers[m - 1]

    if (m == le - 1 or pivot >= list_of_integers[m + 1]) and\
            (m == 0 or pivot >= left):
        return pivot
    elif m != le - 1 and list_of_integers[m + 1] > pivot:
        return (find_peak(list_of_integers[m + 1:]))
    return (find_peak(list_of_integers[:m]))
