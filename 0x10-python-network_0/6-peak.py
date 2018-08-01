#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Python function to find peak number"""
    le = len(list_of_integers)
    if le == 0:
        return
    m = le // 2
    pivot = list_of_integers[m]
    right = list_of_integers[m + 1]
    left = list_of_integers[m - 1]

    if pivot >= left and pivot >= right:
        return pivot
    if right >= pivot:
        return (find_peak(list_of_integers[m:]))
    return (find_peak(list_of_integers[:m]))
