#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    j = 0
    k = ""
    for key, value in a_dictionary.items():
        if value > j:
            j = value
            k = key
    return k
