"""
Write a Python program to test whether a passed letter is a vowel or not.
"""


def is_vowel(t):
    vowel = ['A', 'E', 'I', 'O', 'U', 'Y', 'W' , 'a' , 'e', 'i', 'o', 'u', 'y', 'w']
    return t in vowel


print(f"a -> {is_vowel('a')}")
print(f"b -> {is_vowel('b')}")
print(f"h -> {is_vowel('h')}")
print(f"I -> {is_vowel('I')}")

