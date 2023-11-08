#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_1 = [i for i in set_1 if i not in set_2]
    diff_2 = [i for i in set_2 if i not in set_1]
    return diff_1 + diff_2
