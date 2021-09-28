""" Write a Python program to store a given dictionary in a json file."""

import json

dictionary = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'},
                           {'firstName': 'Mervin', 'lastName': 'Friedland'},
                           {'firstName': 'Aron ', 'lastName': 'Wilkins'}],
              'teachers': [{'firstName': 'Amberly', 'lastName': 'Calico'},
                           {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

print(dictionary)
print(type(dictionary))

#Konwertowanie
json_object = json.dumps(dictionary, indent=2)
print(json_object)
print(type(json_object))

#zapisywanie do pliku JSON

with open('json_files/dicto', 'w') as file:
    json.dump(dictionary, file, indent=2, sort_keys=True)

with open('json_files/dicto') as file:
    data = json.load(file)
    print(data)

