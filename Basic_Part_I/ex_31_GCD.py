"""Write a Python program to compute the greatest common divisor (GCD) of two positive integers"""

import math

def GCD(a,b):
    if (b == 0):
        return a
    return GCD(b, a%b)

def GCD2(a,b):
    return math.gcd(a,b)


print(GCD(36,60))
print(GCD2(48,60))