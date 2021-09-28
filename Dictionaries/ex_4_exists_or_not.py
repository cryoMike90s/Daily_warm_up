"""Write a Python script to check whether a given key already exists in a dictionary."""

avaiable_parts = {'1': "computer",
                  '2': "monitor",
                  '3': "keyboard",
                  '4': "mosue",
                  '5': "hdmi cable",
                  '6': "dvd drive"}

#Solution 1

entered_key = "5"
if entered_key in avaiable_parts:
    print("Yes, is here")
else:
    print("No")