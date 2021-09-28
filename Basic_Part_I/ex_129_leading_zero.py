"""Write a Python program to add leading zeroes to a string."""

def some_zeros(string:str):
    if string[0] != '0':
        return print("{}{}".format(0, string))
    else:
        return print(string)


string = "elomod"
some_zeros(string)