"""
Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum.
"""


def sum_numbers(x, y, z) -> float:
    if x == z == y:
        return (x + z + y) * 3
    return x + y + z


print(f"sum of 3, 4, 5 -> {sum_numbers(3, 4, 5)}")
print(f"sum of 1, 2, 3 -> {sum_numbers(1, 2, 3)}")
print(f"sum of 3, 3, 3 -> {sum_numbers(3, 3, 3)}")
