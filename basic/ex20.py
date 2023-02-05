"""
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
"""


def copies_of_text(n: int, text: str):
    result: str = ""
    for x in range(n):
        result += text
    return result


print(f".text copied 3 times -> {copies_of_text(3,'.text')}")
print(f"abc copied 2 times -> {copies_of_text(2,'abc')}")