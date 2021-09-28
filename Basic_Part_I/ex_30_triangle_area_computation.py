"""Write a Python program that will accept the base and height of a triangle and compute the area."""

def Triangle_area(a,h):
    if a>0 and h>0:
        P = (a*h)/2
        return P
    else:
        print("Base or height must be non zero")


print(Triangle_area(2,3))