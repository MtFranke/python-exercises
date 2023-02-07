"""
Write a Python program to sum three given integers.
However, if two values are equal, the sum will be zero
"""

n1 = 5
n2 = 7
n3 = 5


def sum_numbers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    return a + b + c


print(sum_numbers(n1, n2, n3))
