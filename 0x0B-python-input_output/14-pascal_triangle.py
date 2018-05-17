#!/usr/bin/python3
"""
14-main - Pascals Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    my_list = [[1]]
    for count in range(1, n):
        row = [1]
        for elem in range(1, count):
            row.append(my_list[count - 1][elem - 1] + my_list[count - 1][elem])
        row.append(1)
        my_list.append(row)
    return my_list
