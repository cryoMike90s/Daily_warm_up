"""Write a Python program to create a dictionary from two lists without losing duplicate values."""

from collections import defaultdict

list_1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list_2 = [1, 2, 2, 3]

temp = defaultdict(set)
print(temp)

for c, i in zip(list_1, list_2):
    temp[c].add(i)

print(temp)






