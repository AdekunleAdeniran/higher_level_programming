#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    suml = 0
    for n in new:
        suml += n
    return (suml)
