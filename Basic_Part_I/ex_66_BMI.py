"""Write a Python program to calculate body mass index."""

def BMI(height, weight):
    return (weight/(height * height)).__round__(2)




print(BMI(1.80, 70))