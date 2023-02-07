"""
Write a Python program to sum two given integers.
However, if the sum is between 15 and 20 it will return 20
"""

a = 1
b = 15


def sum_numbers(n1, n2):
    if 15 <= n1 + n2 <= 20:
        return 20
    return n1 + n2


print(sum_numbers(a, b))
