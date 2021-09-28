"""Write a Python program to check whether multiple variables have the same value."""

lista_1 = [1,2,6,3,4,5,6]

def Check_duplicates(lista:list):
    for elem in lista:
        if lista.count(elem) > 1:
            return print("List has some duplicates")
    return print("No duplicates here")


Check_duplicates(lista_1)
