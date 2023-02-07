"""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""
import math


def gcd1(n1, n2):
    print(f"{n1} and {n2} greatest common divisor is {math.gcd(n1, n2)}")


a = 112
b = 24

gcd1(a, b)
