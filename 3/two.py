#!/usr/bin/python3

def chr_to_prio(c):
    if c.isupper():
        return ord(c) - 38
    elif c.islower():
        return ord(c) - 96
    else:
        raise Exception("Invalid condition met")

def get_input(filename):
    f = open(filename, mode='r')
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    return lines

def main():
    file_input_lines = get_input("./input1.txt")

    final = 0
    for i in range(0, len(file_input_lines), 3):
        first, second, third = [set(x) for x in file_input_lines[i:i+3]]
        groupId = list(first.intersection(second).intersection(third))[0]
        final += chr_to_prio(groupId)        

    print(final)

if "__main__" in __name__:
    main()