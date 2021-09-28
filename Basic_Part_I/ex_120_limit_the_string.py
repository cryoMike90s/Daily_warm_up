""" Write a Python program to format a specified string limiting the length of a string"""

def limit_my_string(string:str, limit:int):
    number_of_char = len([x for x in string])
    if number_of_char <= limit:
        return print(string)
    else:
        return print(string[:limit])

limit_my_string("Brutus to atencjusz", 10)
