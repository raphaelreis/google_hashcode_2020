import pandas as pd
import numpy as np


class PizzaProblem():
    pizzas = np.NaN ## contains array with pizzas
    M = 0 # number of slices
    N = 0 #number of pizzas
    chosenPizzas = [] # list with index of chosen pizzas
    score = 0
    def __init__(self,file_name):
        self.read_input(file_name)

    def read_input(self,file_name):
        """TODO: parse input"""
        with open(file_name) as f:
            self.M,self.N = f.readline().split()
            self.M = int(self.M)
            self.N = int(self.N)
            self.pizzas = np.array(f.readline().split()).astype(int)
    def findPizzasRecursive(self):
        """TODO: sort pizzas in descending order. Implement dynamic programming top_down"""
    def findPizzasBottomUp(self):
        """TODO: sort pizzas in descending order. Implement bottom_up DP """
    def printOutput(self):
        """TODO: Print output in form of submission file """
        print(len(self.chosenPizzas))
        print(" ".join(self.chosenPizzas))
if __name__ == "__main__":
    pizzas = PizzaProblem('a_example.in')

