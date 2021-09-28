"""Write a Python program to calculate midpoints of a line"""

def midpoint(p1,p2):
    return ((p1[0]+p2[0])/2), ((p1[1]+p2[1])/2)


p1 = [1, 3]
p2 = [4, 8]

print(midpoint(p1, p2))