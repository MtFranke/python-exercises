"""
Write a Python program to check whether a file exists
"""

import os

path = "/Users/mateusz/Downloads/pit.pdf"
result = os.path.isfile(path)
print(result)
