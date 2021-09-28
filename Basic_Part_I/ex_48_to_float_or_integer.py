"""Write a Python program to parse a string to Float or Integer."""


def Int_or_Float(string):
    x = string.split('.')
    if len(x) > 1:
        return float(string)
    return int(string)


print(Int_or_Float("42.4"))
print(type(Int_or_Float("42.4")))