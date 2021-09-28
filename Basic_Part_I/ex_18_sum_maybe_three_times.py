def calculate_me(liczby):
    if all(x == liczby[0] for x in liczby):
        Z = sum(liczby)*3
    else:
        Z = sum(liczby)
    return Z

liczby= [2,2,2]
print(calculate_me(liczby))