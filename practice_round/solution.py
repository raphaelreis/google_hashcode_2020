import pandas as pd
import numpy as np


class PizzaProblem():
    pizzas = np.NaN ## contains array with pizzas
    M = 0 # number of slices
    N = 0 #number of pizzas
    chosenPizzas = np.NaN
    score = 0
    def __init__(self,file_name):
        self.read_input(file_name)

    def read_input(self,file_name):
        """TODO: parse input"""
        with open(file_name) as f:
            M,N = f.readline().split()
            pizzas = np.array(f.readline().split())

    def findPizzasRecursive(self):
        """TODO: sort pizzas in descending order. Implement dynamic programming top_down"""
    def findPizzasBottomUp(self):
        """TODO: sort pizzas in descending order. Implement bottom_up DP """
    def printOutput(self):
        """TODO: Print output in form of submission file """
        print(len(self.chosenPizzas))
        print()
if __name__ == "__main__":
    pizzas = PizzaProblem('a_example.in')

