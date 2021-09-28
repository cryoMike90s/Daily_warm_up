"""Write a Python program to combine two dictionary adding values for common keys."""

from collections import Counter


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d1_counter = Counter(d1)
d2_counter = Counter(d2)
print(d1_counter)

add = d1_counter + d2_counter
dict3 = dict(add)
print(dict3)

