"""Write a Python program to combine values in python list of dictionaries."""

from collections import Counter

list_dictionary = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]


for dictionaries in list_dictionary:
    print(dictionaries["item"])

result = Counter()

for dictionaries in list_dictionary:
    result[dictionaries['item']] += dictionaries['amount']
print(result)


