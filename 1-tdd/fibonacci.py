# define your solution
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Negative numbers not allowed")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a

