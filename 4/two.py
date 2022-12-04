#!/usr/bin/python3

def get_input(filename):
    f = open(filename, mode='r')
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))

    res = []
    for line in lines:
        one, two = line.split(',')
        res.append([[int(x) for x in one.split('-')], [int(x) for x in two.split('-')]])
    return res

def main():
    file_input_lines = get_input("./input1.txt")

    cnt = 0    
    for pair in file_input_lines:
        pair = sorted(pair, key=lambda x: x[0])

        one, two = pair

        if one[1] >= two[0]:
            cnt += 1 

    print(cnt)
    

if "__main__" in __name__:
    main()