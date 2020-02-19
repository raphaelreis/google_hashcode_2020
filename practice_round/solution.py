import pandas as pd
import numpy as np
import sys

class PizzaProblem():
    pizzas = np.NaN #contains array with pizzas
    M = 0 #number of slices
    N = 0 #number of pizzas
    K = 0 #Number of chosen pizzas
    max_scores = 0 # np array with max score for a number of pizzas K
    c = 0 #np array with optimal cut
    sorted_pizzas=0 #np array with sorted input
    sorted_args = 0 #np array with sorted arguments
    chosenPizzas =[] # list with index of chosen pizzas
    score = 0
    def __init__(self,file_name):
        self.read_input(file_name)
        self.max_scores = np.zeros(self.M+1)
        self.c = self.max_scores.copy()
    def read_input(self,file_name):
        """TODO: parse input"""
        with open(file_name) as f:
            self.M,self.N = f.readline().split()
            self.M = int(self.M)
            self.N = int(self.N)
            self.pizzas = np.array(f.readline().split()).astype(int)

    def solution(self):
        """TODO: sort pizzas in descending order. Implement dynamic programming top_down"""
        self.sorted_pizzas = -np.sort(-self.pizzas)
        self.sorted_idx = np.argsort(-self.pizzas)
        self.score = self.recursive_solution(self.sorted_pizzas,self.M,0)
        #self.findPizzasBottomUp()
    def recursive_solution(self,sorted_pizzas,M,i):

        if M<0:
            return 0
        if sorted_pizzas.size==0:
            return 0
        if sorted_pizzas[0] > M:
            return self.recursive_solution(sorted_pizzas[1:],M,i+1)
        score1 = sorted_pizzas[0] + self.recursive_solution(sorted_pizzas[1:], M - sorted_pizzas[0],i+1)
        if score1 > M:
            score1 = 0
        score2 = self.recursive_solution(sorted_pizzas[1:], M,i+1)
        if score1 > score2:
            self.chosenPizzas.append(i)
            return score1
        else:
            return score2

        #return max(sorted_pizzas[0] + self.recursive_solution(sorted_pizzas[1:], M - sorted_pizzas[0])
         #          ,self.recursive_solution(sorted_pizzas[1:], M))
    def findPizzasBottomUp(self):
        """TODO: sort pizzas in descending order. Implement bottom_up DP """
        for sub_length in range(1,self.M+1):
            max = 0
            for cut in range(self.sorted_pizzas.size): #cut contains index of array
                score = self.sorted_pizzas[cut] + self.c[sub_length-self.sorted_pizzas[cut]]
                if score > sub_length:
                    break
                if score>max:
                    self.c[sub_length] = cut
                    max = score
            self.max_scores[sub_length] = max
        self.score = self.max_scores[-1]
    def reconstruct_solution(self):
        sol = []
        score = self.score
        for pizza_type in reversed(self.chosenPizzas):
            sol.append(self.sorted_args[pizza_type]) #append real index in original list
            score = score - self.sorted_pizzas[pizza_type]
            if score==0:
                break
        return sol
    def printOutput(self):
        """TODO: Print output in form of submission file """
        print(len(self.score))
        print(" ".join(self.c))
    def printInput(self):
        print(self.M,self.N)
        print(self.pizzas)
        return
if __name__ == "__main__":
    pizzas = PizzaProblem('a_example.in')

