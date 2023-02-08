"""
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5
"""


def sum_with_custom_logic(n1, n2):
    if n1 == n2 or n1 + n2 == 5 or abs(n1 - n2) == 5:
        return True

    return False


print(sum_with_custom_logic(5, 5))
print(sum_with_custom_logic(5, 15))
print(sum_with_custom_logic(2, 3))
print(sum_with_custom_logic(2, 7))

