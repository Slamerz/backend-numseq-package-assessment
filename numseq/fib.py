def fib(n):
    """Returns the nth number in the fibonacci sequence: Fn = Fn-1 + Fn-2"""
    sequence = [1, 1]
    if n == 0:
        return 0
    if n < 2:
        return sequence[n]
    for index in range(2, n):
        sequence.append(sequence[index - 1] + sequence[index - 2])
    return sequence.pop()
