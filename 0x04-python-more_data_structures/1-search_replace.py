#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for n in my_list:
        if n == search:
            new.append(replace)
        else:
            new.append(n)
    return(new)
