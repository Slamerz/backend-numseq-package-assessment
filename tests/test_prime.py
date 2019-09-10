import unittest
from numseq.prime import primes, is_prime


class TestPrime(unittest.TestCase):
    def test_is_prime_through_ten(self):
        correct = [False, False, True, True, False, True, False, True, False, False, False]
        for i in range(11):
            self.assertEqual(correct[i], is_prime(i)), \
            "Expected is_prime({}) to equal {}".format(i, correct[i])

    def test_primes(self):
        correct_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEquals(correct_primes, primes(100))
        self.assertEquals(correct_primes[0:10], primes(30))


if __name__ == '__main__':
    unittest.main()
