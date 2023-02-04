"""
Program for generating passwords
"""
import random

lowerLetters = "abcdefghilmnopqrstuvwxyz"
upperLetters = "ABCDEFGHILMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols ="!@#$%^&*(){}[]<>"

chars = lowerLetters + upperLetters + numbers + symbols
length = 16

password = "".join(random.sample(chars, length))
print(password)
