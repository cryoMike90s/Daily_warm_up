""" Write a Python program to concatenate all elements in a list into a string and return it."""

def concat_and_return(lista):
    return ''.join([str(x) for x in lista])


lista = [1,2,4,5]

print(concat_and_return(lista))