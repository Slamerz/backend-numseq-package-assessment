# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: Tests the numseq modules functions.

"""
__author__ = "Jacob Walker"


import sys
from numseq.fib import fib
from numseq.geo import square, triangle, cube
from numseq.prime import is_prime, primes


def print_fib():
    """Print the results of the fibonacci functions"""
    print("Fibonacci")
    for i in range(10):
        print("{}: {}".format(i, fib(i)))
    return 0


def print_geo():
    """Print the results of the Geometric functions"""
    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))


def print_primes():
    """Print the results of the Prime functions"""
    print("Primes")
    prime_list = primes(1000)
    for p in prime_list[-10:]:
        print(p)
    print("Is 999981 prime? {}".format(is_prime(999981)))
    print("Is 999983 prime? {}".format(is_prime(999983)))


def main(args):
    """Print out some tests of the module functions"""
    print_fib()
    print_geo()
    print_primes()


if __name__ == '__main__':
    print("Command line arguments: {}".format(sys.argv))
    status = main(sys.argv)
    sys.exit(status)
