"""
Write a Python program that displays your name, age, and address on three different lines.
"""
import datetime


def print_me():
    name, address = "Mateusz", "Poland, Wrocław"
    age = int(datetime.datetime.now().year) - 1991
    print("Name: {}\nAge: {}\nAddress: {} ".format(name, age, address))


print_me()
