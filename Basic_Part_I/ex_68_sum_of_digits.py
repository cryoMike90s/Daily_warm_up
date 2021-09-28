"""Write a Python program to calculate the sum of the digits in an integer."""

def sum_of_digits(number):
    z = str(number)
    x = z.split('.')[1:]
    y = ''.join(x)
    z1 = 0
    for digit in y:
        elo = int(digit)
        z1 = z1 + elo
    return z1

print(sum_of_digits(10.2522))



def sum_of_digits_2(number):
    return sum([int(z) for z in ''.join((str(number)).split('.')[1:])])

print(sum_of_digits_2(10.2522))



#Rozwiązanie na stronce
num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)