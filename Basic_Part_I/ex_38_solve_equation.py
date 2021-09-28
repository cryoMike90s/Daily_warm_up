"""Write a Python program to solve (x + y) * (x + y)."""

def solve_me(x, y):
    Z = (x + y)*(x + y)
    return print("({} + {})^2 = {}".format(x,y,Z))

x = 4
y = 3

solve_me(x,y)