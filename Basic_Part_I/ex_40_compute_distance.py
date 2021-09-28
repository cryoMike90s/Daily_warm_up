""" Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)."""

import math

def easy_distance(p1,p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

p1 = [1,2]
p2 = [4,5]

print(easy_distance(p1,p2))