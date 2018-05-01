#!/usr/bin/pytho3
def safe_print_list_integers(my_list=[], x=0):
    count = index_check = 0

    while count < x:
        try:
            if type(my_list[count]) is int:
                print("{:d}".format(my_list[count]), end="")
                index_check += 1
            count += 1
        except IndexError:
            raise
    print()
    return index_check
