"""Write a Python program to swap two variables."""

def swap_me(var_1, var_2):
    var_1, var_2 = var_2, var_1
    return print("var_1 is {} and var_2 is {}".format(var_1, var_2))

var_1 = 10
var_2 = 50

print(swap_me(var_1, var_2))