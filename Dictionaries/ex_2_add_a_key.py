"""Write a Python script to add a key to a dictionary."""

avaiable_parts = {'1': "computer",
                  '2': "monitor",
                  '3': "keyboard",
                  '4': "mosue",
                  '5': "hdmi cable",
                  '6': "dvd drive"}

avaiable_parts['7'] = "headphones"

for key, values in avaiable_parts.items():
    print(key, values, sep=", ")