import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    return base ** exponent


def square_root(n):
    if n < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(n)


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def is_even(n):
    return n % 2 == 0


def is_positive(n):
    return n > 0


def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be integer")

    if n < 0:
        raise ValueError("Negative numbers not allowed")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)
