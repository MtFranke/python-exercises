"""
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
import datetime

firstDate = datetime.date(2014, 7, 2)
secondDate = datetime.date(2014, 7, 11)
days = abs((firstDate - secondDate).days)

print(f"{days} days")