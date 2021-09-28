"""Write a Python program to convert the distance (in feet) to inches, yards, and miles."""

def converts_me(distance):
    return print("{} feets equal to {} inches or {} yards or {} miles".format(
        distance, 12*distance, 0.333333*distance, 0.000189394*distance)
    )


converts_me(150)