"""Write a Python program to determine profiling of Python programs."""

import cProfile

def easy_sum(a,b):
    return print(a+b)

easy_sum(333333333333333,111111111111111111111111111111111111111111111111)

cProfile.run('easy_sum(1,2)')