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
        self.max_scores = [[0]]
        self.c = np.zeros(self.N+1)
    def read_input(self,file_name):
        """TODO: parse input"""
        with open(file_name) as f:
            self.M,self.N = f.readline().split()
            self.M = int(self.M)
            self.N = int(self.N)
            self.pizzas = np.array(f.readline().split()).astype(int)

    def solution(self):
        """TODO: sort pizzas in descending order. Implement dynamic programming top_down"""
        #self.sorted_pizzas = -np.sort(-self.pizzas) #use for recursive
        self.sorted_pizzas = np.sort(self.pizzas)
        self.sorted_idx = np.argsort(self.pizzas)
        #self.score = self.recursive_solution(self.sorted_pizzas,self.M,0,[])
        self.findPizzasBottomUp()
    def recursive_solution(self,sorted_pizzas,M,i,path):

        if M<0:
            return [0,path]
        if sorted_pizzas.size==0:
            return [0,path]
        if sorted_pizzas[0] > M:
            return self.recursive_solution(sorted_pizzas[1:],M,i+1,path)
        score1 =self.recursive_solution(sorted_pizzas[1:], M - sorted_pizzas[0],i+1,path.copy())
        score1[0] = sorted_pizzas[0] + score1[0]
        if score1[0] > M:
            score1[0] = 0
        score2 = self.recursive_solution(sorted_pizzas[1:], M,i+1,path.copy())
        if score1[0] > score2[0]:
            score1[1].append(i)
            return score1
        else:
            return score2

        #return max(sorted_pizzas[0] + self.recursive_solution(sorted_pizzas[1:], M - sorted_pizzas[0])
         #          ,self.recursive_solution(sorted_pizzas[1:], M))
    def findPizzasBottomUp(self):
        """TODO: sort pizzas in descending order. Implement bottom_up DP """
        max = 0
        for sub_size in range(1,self.N+1):
            val = self.sorted_pizzas[sub_size-1]
            sub_scores =  []
            for i,prev_scores in enumerate(self.max_scores):
                for j,prev_score in enumerate(prev_scores):
                    score = val+prev_score
                    if score>self.M:
                        score = 0
                    sub_scores.append(score)
                    #self.c.append([i,j])
                    if score > max:
                        max = score
                        self.c = [i,j]
            #sub_scores.append(self.max_scores[sub_size-1][0]) #append first element of previous list
            self.max_scores.append(sub_scores)
        self.score = max
    def reconstruct_solution_recursive(self):
        output = ''
        sol = []
        score = (self.score[0])
        chosen_pizzas = self.score[1]
        for pizza_type in chosen_pizzas:
            sol.append(self.sorted_idx[pizza_type]) #append real index in original list
            score = score - self.sorted_pizzas[pizza_type]
            if score==0:
                break
        output = output+str(self.score[0])
        output = output+'\n'
        output = output+" ".join(map(str,sorted(sol)))
        return output
    def reconstruct_solution_bottom_up(self):
        output = ''
        sol = [item for sublist in self.max_scores for item in sublist]
        idx = np.argmax(sol)
        used_pizzas = list(map(bool,list(reversed(list(bin(idx)[2:]))))) # corresponds to indexes of solution
        final_sol = self.sorted_idx[used_pizzas]
        final_sol = map(str, sorted(final_sol))
        output = output + str(self.score[0])
        output = output + '\n'
        output = output + " ".join(map(str, sorted(sol)))
        return output



    def printInput(self):
        print(self.M,self.N)
        print(self.pizzas)
        return
if __name__ == "__main__":
    pizzas = PizzaProblem('a_example.in')
>>>>>>> cb5c0618dffa55bbcd635a0ef311627f8cef3229

