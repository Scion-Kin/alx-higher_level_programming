#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        def divider(x, y):
            try:
                remainder = x / y
                return remainder

            except ZeroDivisionError:
                return None
        z = divider(a, b)
        return a / b

    except ZeroDivisionError:
        return None

    finally:
        print("Inside result: {}".format(z))
