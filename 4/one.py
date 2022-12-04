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
        one, two = pair
        
        smaller = None
        larger = None

        one_diff = one[1] - one[0]
        two_diff = two[1] - two[0]

        if one_diff > two_diff:
            smaller = two
            larger = one
        else:
            smaller = one
            larger = two

        if smaller[0] >= larger[0] and smaller[1] <= larger[1]:
            cnt+=1

    print(cnt)
    



if "__main__" in __name__:
    main()