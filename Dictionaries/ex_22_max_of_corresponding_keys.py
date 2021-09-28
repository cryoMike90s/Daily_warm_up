"""Write a Python program to find the highest 3 values of corresponding keys in a dictionary."""

from heapq import nlargest


#cwiczenie bubble sort

d1 = {'a': 600, 'b': 200, 'c':100, 'd':400, 'e':500}


def bubble_sort2(dictionary:dict):
    n = len(dictionary.values())
    lista = []

    for x, y in dictionary.items():
        lista.append((x, y))

    for i in range(n -1):
        for j in range(n-1):
            if lista[j][1] > lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


do_rev = bubble_sort2(d1)

for z in do_rev[::-1][0:3]:
    print(z)


#Rozwiązanie


my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)