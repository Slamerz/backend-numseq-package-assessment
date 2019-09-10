import unittest
from numseq.fib import fib


class TestFibonacci(unittest.TestCase):
    def one_through_twenty(self):
        correct = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
        for i in range(20):
            self.assertEqual(correct[i], fib(i))


if __name__ == '__main__':
    unittest.main()
