"""Write a Python program to map two lists into a dictionary."""

lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = ["xd1", "xd2", "xd3", 'xd4', 'xd5', 'xd6']


dic = dict(zip(lista_1, lista_2))
print(dic)

dictionary = {}
for key in lista_1:
    for value in lista_2:
        dictionary[key] = value
        lista_2.remove(value)
        break

print(dictionary)