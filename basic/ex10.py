"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

n = input("Please provide integer to calculate n+nn+nnn of that number : ")
nn = n + n
nnn = n + n + n
result = int(n) + int(nn) + int(nnn)
print(result)
