"""Write a Python program to check multiple keys exists in a dictionary."""

vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'elowa': 'Yamaha XV250'}

print(vehicles.keys() >= {"dream", 'elowa'})
print(vehicles.keys() >= {'tenere', 'jimny', 'xd'})
