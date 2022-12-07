#!/usr/bin/python3

import re

class TreeNode:
    def __init__(self, parent, type, name, size=-1) -> None:
        self.type = type # 'dir' or 'file'
        self.name = name
        self.size = size # 'size will default to 0 while building the tree
        self.children = []
        self.parent = parent

    def calculate_size(self):
        if self.type == "file":
            return self.size

        children_sizes = []
        for child in self.children:
            size = child.calculate_size()
            children_sizes.append(size)
        
        my_size = sum(children_sizes)
        self.size = my_size
        return my_size

    def get_size_sum_of_directories_with_size_less_than_n(self, n):
        if self.type == "file":
            return 0
        
        s = 0
        for child in self.children:
            s += child.get_size_sum_of_directories_with_size_less_than_n(n)

        if self.size <= n:
            s += self.size
        
        return s

    def get_smallest_node_greater_than_n(self, n):
        if self.type == "file":
            return None

        candidates = []
        if self.size >= n:
            candidates.append(self.size)
        
        for child in self.children:
            smallest = child.get_smallest_node_greater_than_n(n)
            if smallest:
                candidates.append(smallest)
        
        if len(candidates) > 0:
            return min(candidates)
        else:
            return None
        
        
    def get_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child

    def _print(self, indent = 0) -> str:
        print(" " *indent + self.name + " size: " + str(self.size))
        for child in self.children:
            child._print(indent+1)

def get_input(filename):
    f = open(filename, mode='r')
    parsed_input = list(map(lambda x: x.strip().split(" "), f.readlines()))
    return parsed_input

def make_tree(terminal_lines):
    _ = terminal_lines.pop(0)
    root = TreeNode(None, "dir", "/")
    curr = root

    for line in terminal_lines:
        if line[0] == "$":
            #command (cd or ls)
            if line[1] == "cd":
                # change dir
                if line[2] == "..":
                    #go up one dir
                    curr = curr.parent
                else:
                    # change directory to one lower
                    dir_name = line[2]
                    curr = curr.get_child(dir_name)
            elif line[1] == "ls":
                # list, noop
                continue
            else:
                raise Exception("Invalid input: ", line)
        elif line[0] == "dir":
            # directory with name 
            dir_name = line[1]

            new_dir_node = TreeNode(curr, "dir", dir_name)
            curr.children.append(new_dir_node)
        elif line[0].isnumeric():
            # file with size, name
            file_size = int(line[0])
            file_name = line[1]

            new_file_node = TreeNode(curr, "file", file_name, file_size)
            curr.children.append(new_file_node)
        else:
            raise Exception("Invalid input: ", line)
    return root

def find_node_to_delete(tree_root: TreeNode, filesystem_size: int, total_needed_space: int):
    used_space = tree_root.size
    free_space = filesystem_size - used_space
    needed_space = total_needed_space - free_space

    print("Needed space: " + str(needed_space))
    
    return tree_root.get_smallest_node_greater_than_n(needed_space)
    

def main():
    terminal_lines = get_input("./input1.txt")
    tree_root = make_tree(terminal_lines)

    tree_root.calculate_size()

    node = find_node_to_delete(tree_root, 70000000, 30000000)

    print("node to remove size: " + str(node))
    

    
if "__main__" in __name__:
    main()