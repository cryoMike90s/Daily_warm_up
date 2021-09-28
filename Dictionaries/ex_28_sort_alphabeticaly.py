"""Write a Python program to sort a list alphabetically in a dictionary."""

num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

for key, values in num.items():
    for value in range(len(values)-1):
        for xd in range(len(values)-1):
            if values[xd] > values[xd+1]:
                values[xd], values[xd+1] = values[xd+1], values[xd]

print(num)