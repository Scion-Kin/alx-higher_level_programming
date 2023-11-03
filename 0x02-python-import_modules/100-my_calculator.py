#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    argc = len(sys.argv) - 1
    
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == "+":
            print(f"{a} {operator} {b} = {calculator_1.add(a, b)}")
        
        elif operator == "-":
            print(f"{a} {operator} {b} = {calculator_1.sub(a, b)}")
        
        elif operator == "*":
            print(f"{a} {operator} {b} = {calculator_1.mul(a, b)}")
        
        elif operator == "/":
            print(f"{a} {operator} {b} = {calculator_1.div(a, b)}")
        
        else:
            print("Unknown operator. Available operators: +, -, * and /")
