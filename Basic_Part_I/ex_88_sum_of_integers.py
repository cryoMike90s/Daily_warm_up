"""Given variables x=30 and y=20, write a Python program to print "30+20=50"."""

def sum_me(x:int, y:int):
    return print('{} + {} = {}'.format(x, y, (x+y)))

sum_me(30, 20)