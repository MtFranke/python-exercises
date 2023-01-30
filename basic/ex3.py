# Write a Python program to display the current date and time.

from datetime import datetime

today = datetime.now()

print(f"Current date and time : {today.strftime('%d-%m-%Y %H:%M:%S')}")
