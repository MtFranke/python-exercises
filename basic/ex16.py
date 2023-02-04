"""
Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference.
"""

givenNumber = int(input("please provide an number to see the difference with number 17: "))

if givenNumber > 17:
    print(givenNumber - 17)
else:
    print(abs(givenNumber-17)*2)

