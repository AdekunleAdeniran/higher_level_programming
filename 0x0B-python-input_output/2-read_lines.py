#!/usr/bin/python3
'''Python function that reads n lines and print ot stdout'''


def read_lines(filename="", nb_lines=0):
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
            print(line, end="")
            if nb_lines == count:
                break
