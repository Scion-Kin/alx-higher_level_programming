#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    result = 0

    for i in range(1, args):
        result += int(sys.argv[i])
        i += 1

    print(result)
