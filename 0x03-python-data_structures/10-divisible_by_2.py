#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = []
    for n in my_list:
        if n % 2 == 0:
            n.append(True)
        else:
            n.append(False)
    return n
