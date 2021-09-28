"""Write a Python program to convert a byte string to a list of integers."""


def convert_me_2(stringi:bytes):
    return [int(a) for a in stringi]

lista = b"abc"

print(convert_me_2(lista))