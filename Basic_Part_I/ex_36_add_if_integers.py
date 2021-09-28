""" Write a Python program to add two objects if both objects are an integer type."""

def both_integers(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    return "One or both values are not integer type"

print(both_integers(1,"a"))