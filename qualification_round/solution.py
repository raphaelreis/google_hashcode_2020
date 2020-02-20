import numpy as np
import pandas as pd


class LibrarySystem:

    def __init__(self,filename):
        self.parse_input(filename)
        self.w = np.array([0,1,2,3]) #need to sort
        self.libs_df = pd.DataFrame(columns=['t','b','b_ids','taken_books','score'])


    def parse_input(self,filename):
        """TODO: Parse input file"""

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
        brute_score = self.w.dot(df.b_ids)
        book_ids = self.sorted_idx[brute_score!=0][-df.b:]
        score = np.sum(brute_score[book_ids])/df.t # Sum of book scores/signup time
        return score


if __name__ == "__main__":
    a =1