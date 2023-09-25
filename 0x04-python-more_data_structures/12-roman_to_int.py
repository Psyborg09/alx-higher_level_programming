#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0
    else:
        my_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                   "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_value = 0
        for character in roman_string[:: -1]:
            current_value = my_dict[character]
            if current_value >= prev_value:
                result = result + current_value
            else:
                result = result - current_value
            prev_value = current_value
        return result
