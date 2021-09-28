"""Write a Python function to check whether a distinct pair of numbers whose product
 is odd present in a sequence of integer values."""


def pair_is_odd_in_list(lista:list, a:int, b:int) -> None:
    c = a + b
    return print("Jest" if c in lista and (c % 2 != 0) else "Nie ma")


lista = [1, 2, 3, 4, 5, 9]
pair_is_odd_in_list(lista, 2, 2)
