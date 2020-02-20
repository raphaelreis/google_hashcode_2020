import numpy as np
import pandas as pd
import sys

def parse_input(file_name):
    """TODO: Parse input file"""
    fo = open(file_name, "r")
    lines = fo.read().splitlines()
    return lines

def get_constants(first_line):
    constants = [int(i) for i in first_line.split()]
    B, L, D = constants[0], constants[1], constants[2]
    return B, L, D

def get_books_weight(second_line):
    W = [int(i) for i in second_line.split()]
    return W

def parse_libraries(s, L):
    t = []
    books_count = []
    b = []
    b_ids = []
    
    for i in range(2, 3 + L, 2):
    
        lib_setup = [int(i) for i in s[i].split()]
        books_count.append(lib_setup[0])
        t.append(lib_setup[1])
        b.append(lib_setup[2])
        b_ids.append([int(i) for i in s[i+1].split()])
    
    return books_count, t, b, b_ids

if __name__ == "__main__":
    file_name = "a_example.txt"

    s = parse_input(file_name)
    B, L, D = get_constants(s[0])
    W = get_books_weight(s[1])
    
    # t = []
    # books_count = []
    # b = []
    # b_ids = []
    
    # for i in range(2, 3 + L, 2):
    #     print(i)
    #     lib_setup = [int(i) for i in s[i].split()]
    #     books_count.append(lib_setup[0])
    #     t.append(lib_setup[1])
    #     b.append(lib_setup[2])
    #     b_ids.append([int(i) for i in s[i+1].split()])

    books_count, t, b, b_ids = parse_libraries(s, L)

    print(books_count, t, b, b_ids)

class LibrarySystem:

    def __init__(self,filename):
        self.parse_input(filename)


    def parse_input(self,filename):
        """TODO: Parse input file"""

    def print_output(self):
        """TODO: Print output as requested"""

