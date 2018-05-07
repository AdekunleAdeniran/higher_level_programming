#!/usr/bin/python3


'''
   5-text_indentation
   Contains a function that adds new line after characters
'''


def text_indentation(text):
    '''Python function to add two new lines to string at character points'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    period = text.replace('.', '.\n\n')
    period = period.replace('?', '?\n\n')
    period = period.replace(':', ':\n\n')
    period1 = period.split('\n')
    for line in range(len(period1)):
        print("{}".format(period1[line].strip()),
              end=("" if (line == (len(period1) - 1)) else '\n'))
