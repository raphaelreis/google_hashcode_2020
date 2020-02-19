import unittest
from practice_round import solution as s

class MyTestCase(unittest.TestCase):

    def test_readInput(self):
        pizzas = s.PizzaProblem('a_example.in')
        self.assertEqual(True, False)

    def test_problema(self):
        """to do"""
        a = s.read_input()


if __name__ == '__main__':
    unittest.main()
