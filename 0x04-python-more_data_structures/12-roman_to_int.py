#!/usr/bin/python3

def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    roms = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ints = [roms[i] for i in roman_string] + [0]
    result = 0

    for i in range(len(ints) - 1):
        if ints[i] >= ints[i+1]:
            result += ints[i]
        else:
            result -= ints[i]

    return result
