#!/usr/bin/python3

import re

def get_input(filename):
    f = open(filename, mode='r')
    raw_input = f.readline().strip()
    return [*raw_input]

def main():
    chars = get_input("./input1.txt")

    last_four = []    
    answer = -1
    for i in range(len(chars)):
        c = chars[i]
        if len(last_four) != 4:
            last_four.append(c)
            continue

        last_four.pop(0)
        last_four.append(c)

        if len(last_four) == len(set(last_four)):
            answer = i
            break

    print(answer+1)

    
if "__main__" in __name__:
    main()