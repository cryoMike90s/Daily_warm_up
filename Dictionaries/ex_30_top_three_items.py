"""Write a Python program to get the top three items in a shop"""

import itertools

dictionary = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}



top_three = dict(itertools.islice(sorted(dictionary.items(), key=lambda x: x[1], reverse=True),3))
for key, value in top_three.items():
    print(key, value)


