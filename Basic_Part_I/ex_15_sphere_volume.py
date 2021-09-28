import math

def sphere_volume(radius):
    V = float(4/3) * math.pi * (radius ** 3)
    return V

print(sphere_volume(6))