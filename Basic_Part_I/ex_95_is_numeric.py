"""Write a Python program to check whether a string is numeric."""

def check_if_numeric(string:str):
    if string.isnumeric():
        print("Yes")
    else:
        print("No")

check_if_numeric("1avsd")