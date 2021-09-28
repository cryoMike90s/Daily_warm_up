""" Write a Python function that takes a positive integer and returns the sum of the cube of all
 the positive integers smaller than the specified number."""



def positive_integers_case(liczby:list, granica:int) -> None:
    pozytywne = []
    kubiki = []
    for x in liczby:
        if x > 0:
            pozytywne.append(x)
    for y in pozytywne:
        if y < granica:
            y = y ** 3
            kubiki.append(y)
    return print(sum(kubiki))


licz = [-1,2,3,4,12]
positive_integers_case(licz, 4)


def positive_integers_case2(liczby:list, granica:int) -> None:
    return sum([x ** 3 for x in liczby if (x > 0) and (x < granica)])

print(positive_integers_case2(licz,4))
