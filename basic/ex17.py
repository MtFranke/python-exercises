"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""


def number_near(n) -> bool:
    return (abs(n - 1000) <= 100) or (abs(n - 2000) <= 100)


print(f"1500 -> {number_near(1500)}")
print(f"800 -> {number_near(800)}")
print(f"900 -> {number_near(900)}")
print(f"1000 -> {number_near(1000)}")
print(f"2050 -> {number_near(900)}")
print(f"-1000 -> {number_near(-1000)}")

