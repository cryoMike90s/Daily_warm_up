""" Write a Python program to convert a list into a nested dictionary of keys."""

lista = ['dupa', 'elo', 'wariacie', 'dzisiaj', 'wtorek']
dictionary = current = {}

for name in lista:
    current[name] = {}
    current = current[name]

print(dictionary)

