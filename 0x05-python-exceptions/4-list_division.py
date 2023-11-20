#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    try:

        new = []

        for i in range(list_length):

            try:
                a = my_list_1[i] / my_list_2[i]
                new.append(a)

            except ZeroDivisionError:
                print("division by 0")
                new.append(0)

            except IndexError:
                print("out of range")
                new.append(0)

            except (TypeError, ValueError):
                print("wrong type")
                new.append(0)

    finally:
        return new
