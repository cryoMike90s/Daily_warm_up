"""Write a Python program to hash a word."""

import hashlib

def hash_me(string):
    hash_object = hashlib.md5(string.encode())
    return print(hash_object.hexdigest())

hash_me("Dupa, elo mordo")