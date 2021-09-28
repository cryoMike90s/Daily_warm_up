""" Write a Python program to filter the positive numbers from a list. """



def only_positive(lista:list):
    return list(filter(lambda x: x > 0, lista))


lista = [1,50,20,-5, -6, 10]
print(only_positive(lista))