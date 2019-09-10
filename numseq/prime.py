def primes(n):
    """Returns all prime numbers less than the nth number"""
    results = []
    for i in range(n):
        if is_prime(i):
            results.append(i)
    return results


def is_prime(m):
    """Returns a boolean for if the mth number is prime"""
    if m > 1:
        for i in range(2, m):
            if m % i == 0:
                return False
        return True
    return False
