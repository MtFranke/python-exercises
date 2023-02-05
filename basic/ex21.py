"""
Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
"""


def is_even(n: int) -> bool:
    return n % 2 == 0


print(f"is_even(21) -> {is_even(21)}")
print(f"is_even(112) -> {is_even(112)}")
print(f"is_even(0) -> {is_even(0)}")
