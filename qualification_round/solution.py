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




class LibrarySystem:

    def __init__(self,filename):
        s = parse_input(file_name)
        self.B, self.L, self.D = get_constants(s[0]) # B: Number of books,L: number of libraries,D: number of days
        books_count, t, b, b_ids = parse_libraries(s, self.L)
        self.w = np.array(get_books_weight(s[1]))
        self.libs_df = pd.DataFrame(zip(t,b,b_ids),columns=['t','b','b_ids'])
        self.libs_df['taken_books'] = 0
        self.libs_df['score']=0



    def print_output(self):
        """TODO: Print output as requested"""



    def setup(self):
        """TODO: Sort book score"""
        self.sorted_w = -np.sort(-self.w)
        self.sorted_idx = np.argsort(self.w)

        # Update indexes in library
        self.libs_df.b = self.libs_df.b_ids.apply(lambda x: x[self.sorted_idx],axis=1)
    def greedy_solution(self):
        """TODO: Iterate over available books, taking largest score at a time. Updating score at every iteration"""

        for day in self.D:
            self.libs_df.score = self.libs_df.apply(self.compute_score,axis=1)
            self.libs_df.sort_values('score')

    def compute_score(self,df:pd.Series):
        """"TODO: Compute score of a given row at a given time step"""
        brute_score = self.sorted_w.dot(df.b_ids)
        book_ids = self.sorted_idx[brute_score!=0][:self.b]
        score = np.sum(brute_score[book_ids])/df.t # Sum of book scores/signup time
        return score


if __name__ == "__main__":
    file_name = "a_example.txt"

    #s = parse_input(file_name)
    system = LibrarySystem(file_name)
    #B, L, D = get_constants(s[0])
    #W = get_books_weight(s[1])

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

    #books_count, t, b, b_ids = parse_libraries(s, L)

    #print(books_count, t, b, b_ids)
