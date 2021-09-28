"""Write a Python program to get the size of an object in bytes."""

import sys

def give_me_size(object):
    return sys.getsizeof(object)

print(give_me_size("Basic_Part_I/ex_59_feet_inches_to_centimeters.py"))