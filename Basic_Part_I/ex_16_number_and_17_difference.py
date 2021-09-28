def odejmowanko(number):
    if number <= 17:
        Z = 17 - number
    else:
        Z = 2* abs(17-number)
    return Z

number = 19
print(odejmowanko(number))