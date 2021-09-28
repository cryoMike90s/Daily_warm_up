""" Write a Python program to check whether lowercase letters exist in a string."""


def check_if_lower(string:str):
    if len([x for x in string if x.islower()]) > 1:
        return print("String contains lowercase letter")
    else:
        return print("String without lowercase letter")





def check_if_lower_v2(string:str):
    for x in string:
        if x.islower():
            print("String contains lowercase letter")
            break
    else:
        return print("String without lowercase letter")


string = "MORDECZKOaa"

check_if_lower(string)
check_if_lower_v2(string)



