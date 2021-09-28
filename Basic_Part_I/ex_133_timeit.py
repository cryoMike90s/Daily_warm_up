""" Write a Python program to calculate the time runs (difference between start and current time) of a program."""

import timeit


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result



if __name__ == "__main__":
    print(timeit.timeit("x=fact(130)", setup="from __main__ import fact", number=10000))