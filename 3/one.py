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

    for line in file_input_lines:
        first, second = line[:int(len(line)/2)], line[int(len(line)/2):]

        first_set = set(first)
        second_set = set(second)
        
        intersect = first_set.intersection(second_set)
        final += chr_to_prio(list(intersect)[0])

    print(final)



if "__main__" in __name__:
    main()