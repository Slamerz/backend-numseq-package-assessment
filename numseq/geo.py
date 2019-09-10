def square(n):
    """Returns the square root of the nth number: n * n"""
    return n ** 2


def triangle(n):
    """Returns the nth triangular number: T = (n)(n + 1) / 2"""
    result = 0
    for i in range(n+1):
        result = result + i
    return result


def cube(n):
    """Returns the cube of the nth number. : n * n * n"""
    return n ** 3
