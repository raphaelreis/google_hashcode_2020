import unittest
from practice_round import solution as s

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    def test_problema(self):
        a = s.read_input()


if __name__ == '__main__':
    unittest.main()
