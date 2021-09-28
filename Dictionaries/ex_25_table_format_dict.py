"""Write a Python program to print a dictionary in table format."""

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

print("{:<8} {:<15}".format("Key", "Value"))
for key, value in vehicles.items():
    print("{:<8} {:<15}".format(key, value))
