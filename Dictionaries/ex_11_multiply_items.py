"""Write a Python program to multiply all the items in a dictionary."""

from math import prod

dic1 = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
#pierwsze rozwiązanie
print(prod(dic1.values()))
print()
#inaczej
result = 1
for x in dic1:
    result = result * dic1[x]

print(result)
