#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    n = []
    for new in a_dictionary:
        n.append(new)
    return max(n)
