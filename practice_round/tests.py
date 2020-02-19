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
        ans = pizzas.reconstruct_solution()
        self.assertEquals((pizzas.score),13)

    def test_output(self):
        pizzas


if __name__ == '__main__':
    unittest.main()
