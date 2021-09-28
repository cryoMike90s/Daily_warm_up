"""Write a Python program to get the Identity, Type, and Value of an object."""

def define_me(object):
    return print("Object id: {}, \nObject type: {}, \nObject value: {}".format(id(object), type(object), object))

define_me("dupa")