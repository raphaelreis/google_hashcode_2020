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
def print_output():
    """TODO: Print output as requested"""


if __name__ == "__main__":
    file_name = "a_example.txt"

    s = parse_input(file_name)
    B, L, D = get_constants(s[0])
    W = get_books_weight(s[1])
    
    
    print(W)