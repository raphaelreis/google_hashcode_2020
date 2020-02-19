import unittest
from practice_round import solution as s

class MyTestCase(unittest.TestCase):

    def test_readInput(self):
        pizzas = s.PizzaProblem('a_example.txt')
        pizzas.printInput()

    def test_problema(self):
        """to do"""
        pizzas = s.PizzaProblem('a_example.txt')
        pizzas.solution()
        print(pizzas.reconstruct_solution())
        output = '16\n0 2 3'
        self.assertEquals(pizzas.reconstruct_solution(),output)

    def test_problemb(self):
        pizzas = s.PizzaProblem('b_small.txt')
        pizzas.solution()
        print(pizzas.reconstruct_solution())
        #output = ''
    def test_problemc(self):
        pizzas = s.PizzaProblem('c_medium.txt')
        pizzas.solution()
        print(pizzas.reconstruct_solution())
        #output = ''
if __name__ == '__main__':
    unittest.main()
