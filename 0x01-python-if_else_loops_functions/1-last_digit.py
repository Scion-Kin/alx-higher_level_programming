#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)
last = int(last[-1])

if last < 6 and not 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last == 0:
    print(f"Last digit of {number} is {last} and is zero")
else:
    print(f"Last digit of {number} is {last} and is greater than 5")
