import pandas as pd
import numpy as np
import math

def read_input(file_name):
    """TODO: parse input"""
    f = open(file_name, "r")
    s = f.read()
    a = [int(i) for i in s.split()]
    return a

def get_struct(a):
    max_slices = a[0]
    types_count = a[1]
    slices = a[2:]

    return max_slices, types_count, slices

def cut_rod(p, n):
    if n == 0:
        return 0
    q = - math.inf
    for i in range(n):
        print("i: %i" %i)
        q = max(q, p[i] + cut_rod(p, n - i - 1))
        print("q: %i" %q)
    return q

def cut_rod_bu(p, n):
    r = [0 for i in range(n)]
    c = [0 for i in range(n)]
    for length in range(0, n):
        max_ = -math.inf
        for cut in range(0, length):
            print("p[length]: ", p[length])
            if p[length] + c[length - cut] > max_:
                c[length] = cut
                max_ = p[cut] + c[length - cut]
        r[length] = max_

    return r[n], c[n]
if __name__ == "__main__":

    file_name = "practice_round/a_example.txt"
    a = read_input(file_name)
    max_slices, types_count, slices = get_struct(a)
    sorted(slices)

    print(f"cut_rod_bu: {cut_rod_bu(slices, max_slices)}")
    # Bottom up
    # 
    # tmp = max_slices
    # solution = [0]
    # for i in range(max_slices):
    #     if i < slices[0]:
    #         solution.append(0)

    #     if i == slices[i]:
    #         tmp = tmp - slices[i]

    # print(solution)

    # print(cut_rod(slices, max_slices))

