"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""

x, y = 4, 3
calc = ((x + y) ** 2)
print("({} + {}) ^ 2 = {}".format(x, y, calc))
