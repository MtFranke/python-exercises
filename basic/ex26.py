"""
Write a Python program to create a histogram from a given list of integers
"""


def print_histogram(array: list[int]):
    for n in array:
        txt = ""
        for x in range(n):
            txt += "@"
        print(txt)


print_histogram([2, 3, 6, 5])
