"""
Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""


def contains(n: int, array: list[int]) -> bool:
    return n in array


print(contains(3, [1, 5, 8, 3]))
print(contains(-1, [1, 5, 8, 3]))
