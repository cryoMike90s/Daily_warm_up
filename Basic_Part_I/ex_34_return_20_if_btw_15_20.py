"""Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20"""

def sumujemy(a,b):
    if (a+b) >= 15 and (a+b) <= 20:
        return 20
    return a + b

print(sumujemy(10,5))