"""Write a Python program to compute the product of a list of integers (without using for loop)."""

from functools import reduce
import math

def prod_without_loop(lista:list):
    return print(math.prod(lista))



def prod_without_loop_v2(lista:list):
    return print(reduce(lambda x, y: x*y, lista))

lista = [2,3,5]
prod_without_loop(lista)
prod_without_loop_v2(lista)