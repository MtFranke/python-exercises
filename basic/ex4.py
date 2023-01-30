# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# A=πr2
import math

pi = math.pi
radius = input('Enter radius of the circle:')
area = pi * (math.pow(float(radius), 2))
print(f"Area is equal to: {area}")

