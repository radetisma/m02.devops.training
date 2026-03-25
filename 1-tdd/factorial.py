# define your solution
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    # Negative number check
    if n < 0:
        raise ValueError("Negative numbers are not allowed!")

    # 0&1 case
    if n == 0 or n == 1:
        return 1

    # Recursion for n > 1
    return n * factorial(n - 1)

