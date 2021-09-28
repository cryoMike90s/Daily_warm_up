"""Write a Python program to calculate the hypotenuse of a right angled triangle."""

import math

def hypo(h,base):
    return math.hypot(h, base)

print(hypo(10,2))