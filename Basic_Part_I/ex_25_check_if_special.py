"""Write a Python program to check whether a specified value is contained in a group of values."""

def check_if(number,list):
    return [print("There is {} in {}".format(number, i)) for i in list if number in i]


list = [[1,3,5,6],[1,7,9,10]]
number = 7

check_if(number,list)
