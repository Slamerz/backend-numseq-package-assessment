import unittest
from numseq.geo import square, triangle, cube


class TestGeometricNumbers(unittest.TestCase):
    def test_square_through_ten(self):
        correct = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        for i in range(10):
            self.assertEqual(correct[i], square(i),
                             "Expected square({}) to equal {}, but got {} instead".format(i, i, correct[i]))

    def test_triangle_through_ten(self):
        correct = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
        for i in range(10):
            self.assertEqual(correct[i], triangle(i),
                             "Expected triangle({}) to equal {}, but got {} instead".format(i, i, correct[i]))

    def test_cube_through_ten(self):
        correct = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
        for i in range(10):
            self.assertEqual(correct[i], cube(i),
                             "Expected cube({}) to equal {}, but got {} instead".format(i, i, correct[i]))


if __name__ == '__main__':
    unittest.main()
