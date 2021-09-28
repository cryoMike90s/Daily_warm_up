"""Write a Python program to get a new string from a given string where "Is" has been added to the front.
 If the given string already begins with "Is" then return the string unchanged"""

def Add_a_string(text):
    if text[0] == 'l' and text[1] == 's' and len(text) >= 2:
        new_string = text
    else:
        new_string = "ls" + text
    return new_string


text = "d"
print(Add_a_string(text))
