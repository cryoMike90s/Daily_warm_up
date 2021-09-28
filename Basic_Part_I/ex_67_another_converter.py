"""Write a Python program to convert pressure in kilopascals to pounds per square inch,
 a millimeter of mercury (mmHg) and atmosphere pressure."""


def convert_me(kilopascals):
    print("{} kilopascals are equal to {} pounds per square inch,"
          " {} milimeter of mercury, {} atmosphere pressure".format(
        kilopascals, (kilopascals * 0.145038).__round__(2),
        (kilopascals * 7.50062).__round__(2),
        (kilopascals * 0.00986923).__round__(3)
    ))


convert_me(int(input("Enter a value of kilopascals: ")))
