"""
Write a Python program to add two objects if both objects are integers.
"""


def add_integers(a, b):
    arg1 = isinstance(a, int)
    arg2 = isinstance(b, int)

    if arg1 is False:
        print("First argument isn't of type integer")

    if arg2 is False:
        print("Second argument isn't of type integer")

    if arg1 and arg2:
        return a + b


print(f"{add_integers(2, 2)}")
print(f"{add_integers(2.1, 2)}")
print(f"{add_integers(2, '2')}")
