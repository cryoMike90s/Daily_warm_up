""" Write a Python program to split a variable length string into variables."""

def split_into_variables(string:str):
    first_name, last_name = string.split()
    return print(first_name, last_name)


split_into_variables("elo wariacie")