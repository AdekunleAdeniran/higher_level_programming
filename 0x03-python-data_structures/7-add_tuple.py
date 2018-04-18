#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    first = tuple_a + ('0', '0')
    second = tuple_b + ('0', '0')

    sum1 = int(first[0]) + int(second[0])
    sum2 = int(first[1]) + int(second[1])
    return(sum1), (sum2)
