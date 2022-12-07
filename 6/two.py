#!/usr/bin/python3

import re

def get_input(filename):
    f = open(filename, mode='r')
    raw_input = f.readline().strip()
    return [*raw_input]

def main():
    chars = get_input("./input1.txt")

    last_fourteen = []    
    answer = -1
    for i in range(len(chars)):
        c = chars[i]
        if len(last_fourteen) != 14:
            last_fourteen.append(c)
            continue

        last_fourteen.pop(0)
        last_fourteen.append(c)

        if len(last_fourteen) == len(set(last_fourteen)):
            answer = i
            break

    print(answer+1)

    
if "__main__" in __name__:
    main()