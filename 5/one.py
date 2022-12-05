#!/usr/bin/python3

import re

def get_input(filename):
    f = open(filename, mode='r')
    
    rows = []
    while f:
        line = f.readline()
        if line.__contains__("1"):
            break

        row_crates = list(map(lambda x: x.replace('[', '').replace(']', '').replace('\n', ''), re.split(r'    |] \[| \[|] ', line)))
        rows.append(row_crates)
    
    stacks = []
    for i in range(0, len(rows[0])):
        stack = []
        for j in range(len(rows)-1, -1, -1):
            if rows[j][i]:
                stack.append(rows[j][i])
        stacks.append(stack)

    instructions = []
    lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        ins = re.split(r'move | from | to ', line)
        ins.remove('')
        ins = list(map(lambda x: int(x), ins))
        instructions.append(ins)
    
    return (stacks, instructions)
    
    

def main():
    stacks, instructions = get_input("./input1.txt")
    print(stacks)

    for ins in instructions:
        qty, src, dest = ins

        # ...gotta offset by one sigh
        src -= 1
        dest -= 1
        for i in range(qty):
            item = stacks[src].pop()
            stacks[dest].append(item)

    for stack in stacks:
        print(stack[-1], end="")
    
if "__main__" in __name__:
    main()