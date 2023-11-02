#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")

    if count == 1:
        print("1 argument:\n1:", sys.argv[1])

    if count > 1:
        print("{} arguments:".format(count))
        for i in range(1, count + 1):
            print(f"{i}: {sys.argv[i]}")
