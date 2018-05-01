#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for items in range(x):
        try:
            print("{:d}".format(my_list[items]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
