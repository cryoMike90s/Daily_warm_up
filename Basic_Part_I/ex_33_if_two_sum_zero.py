"""Write a Python program to sum of three given integers. However, if two values are equal sum will be zero"""

def Sumujemy(a,b,c):
    if a == b or b == c or c == a:
        return 0
    else:
        return a+b+c


print(Sumujemy(3,2,3))
