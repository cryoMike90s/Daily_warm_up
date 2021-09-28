""" Write a Python program to remove spaces from dictionary keys."""

vehicles = {
    ' dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    ' er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'elowa': 'Yamaha XV250'}


vehicles2 = {}

for key, values in vehicles.items():
    vehicles2[key.strip()] = values

print(vehicles2)