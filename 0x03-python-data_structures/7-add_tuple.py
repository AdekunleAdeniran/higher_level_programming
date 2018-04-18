#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_a) == 1:
        tuplea1 = [tuple_a[0], 0]
        tuple_a = tuple_a1[0], tuple_a1[1]
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_b) == 1:
        tuple_b1 = [tuple_b[0], 0]
        tuple_b = tuple_b1[0], tuple_b1[1]
    z = []
    for i in range(len(tuple_a)):
        z.append(tuple_a[i] + tuple_b[i])
    return tuple(z)
