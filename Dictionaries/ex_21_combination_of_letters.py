"""Write a Python program to create and display all combinations of letters,
 selecting each letter from a different key in a dictionary. """

import itertools

dictionary = {'1':['a','b'], '2':['c','d']}

for combo in itertools.product(*[dictionary[k] for k in sorted(dictionary.keys())]):
    print("".join(combo))

#inaczej






print()
#Treningowo

lista_1 = [1,2,3,4]
lista_2 = [5,6,7,8]

#Rozwiązanie 1
a = itertools.product(lista_1,lista_2)
for x in a:
    print(x)

print()
#Rozwiązanie 2

b = [(x, y) for x in lista_1 for y in lista_2]
for z in b:
    print(z)
