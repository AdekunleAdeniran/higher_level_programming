#!/usr/bin/python3


'''
   5-text_indentation
   Contains a function that adds new line after characters
'''


def text_indentation(text):
    '''Python function to add two new lines to string at character points'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    dxt = ['?', '.', ':']
    new = ""
    for items in text:
        new += items
        if items in dxt:
            new += '\n'
            print(new.strip(" "))
            new = ""
    if items not in dxt:
        print(new.strip(" "))
