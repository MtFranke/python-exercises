"""
Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
Return n copies of the whole string if the length is less than 2
"""


def copies_of_two_first_letters(txt, n):
    two_letters = txt[:2]
    result = ""
    for x in range(n):
        result += two_letters
    print(result)


copies_of_two_first_letters("python", 2)
copies_of_two_first_letters("d", 2)
