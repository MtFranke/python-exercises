"""
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

import math
p1 = [4, 0]
p2 = [6, 6]
distance1 = (p1[0]-p2[0]) ** 2
distance2 = (p1[1]-p2[1]) ** 2

distance = math.sqrt(distance1 + distance2)

print(distance)