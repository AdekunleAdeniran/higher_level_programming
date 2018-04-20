#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    items = 0
    if type(roman_string) is not str or len(roman_string) is 0:
        return 0
    for items in range(items, len(roman_string)):
        if items < len(roman_string) -1 and dic[roman_string[items]] < dic[roman_string[items + 1]]:
            result -= dic[roman_string[items]]
        else:
            result += dic[roman_string[items]]
    return result
