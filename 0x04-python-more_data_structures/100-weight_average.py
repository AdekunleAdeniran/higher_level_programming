#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    suma = sumb = product = average = 0
    for tuple in my_list:
        suma += tuple[1]
        product = tuple[0] * tuple[1]
        sumb += product
        average = sumb / suma
    return average
