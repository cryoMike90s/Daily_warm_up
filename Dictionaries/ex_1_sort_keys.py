""" Write a Python script to sort (ascending and descending) a dictionary by value."""

avaiable_parts = {'1': "computer",
                  '2': "monitor",
                  '3': "keyboard",
                  '4': "mosue",
                  '5': "hdmi cable",
                  '6': "dvd drive"}


sortowanko = sorted(avaiable_parts.values())
print(sortowanko)


sortowanko2 = sorted(avaiable_parts.values(), reverse=True)
print(sortowanko2)



#Tutaj poprawnie

sortowanko_v2 = dict(sorted(avaiable_parts.items(), key=lambda x:x[1]))
print(sortowanko_v2)
print(type(sortowanko_v2))

sortowanko2_v2 = dict(sorted(avaiable_parts.items(),key=lambda x:x[1], reverse=True))
print(sortowanko2_v2)
print(type(sortowanko2_v2))