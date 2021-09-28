"""Write a Python program to empty a variable without destroying it."""

n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
elo = 15

print(type(n)())
print(type(d)())
print(type(l)())
print(type(t)())

z = type(elo)()
print(z)