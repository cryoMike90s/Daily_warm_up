""" Write a Python program to print all even numbers from a given numbers list in the same order and stop the
printing if any numbers that come after 237 in the sequence"""


def print_even(numbers):
    for i in numbers:
        if i == 237:
            break
        else:
            if i % 2 == 0:
                print(i)


def print_even_differently(numbers):
    return [i for i in iter(lambda x =iter(numbers): next(x), 237) if i % 2 == 0]

    #Powyżej:
    #1) Należy przekonwertować podaną liste liczb do iteratora, uzyty x=iter(numbers), który posłuży jako pożywka xd dla lambdy
    #2) Nastepnie trzeba ustawić strażnika, którym jest liczba 237 aby zatrzymało iteracje
    # Ogólnie to chyba dzięki temu iter(lamb...) mozna ominać wcześniejsze problemy jak brak nadlisty xd
    #WAZNE tutaj to jest taki myk, że on leci tym iteratorem z iter(lambda...) po tych iteratorach z iter(numbers)
    # i jak widzi iterator taki jak jest ustawiony sentiel to robi break

def print_even_differently_v2(numbers):
    return [n for n in numbers[:numbers.index(237)] if n % 2 == 0]



numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
]

print_even(numbers)
print(print_even_differently(numbers))
print(print_even_differently_v2(numbers))

print(30*"*")
x = iter(numbers)
y = print(next(x))
z = print(next(x))
