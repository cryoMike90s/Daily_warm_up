"""Write a Python program to convert true to 1 and false to 0. """

def convert_me(x):
    if bool(x) == False:
        return print(0)
    else:
        return print(1)

convert_me([3])