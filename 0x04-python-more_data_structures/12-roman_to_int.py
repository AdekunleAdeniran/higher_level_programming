#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    item = 0
    roman = roman_string
    if type(roman) is not str or len(roman) is 0:
        return 0
    for item in range(item, len(roman)):
        if item < len(roman) - 1 and dic[roman[item]] < dic[roman[item + 1]]:
            result -= dic[roman[item]]
        else:
            result += dic[roman[item]]
    return result
