"""Write a Python program to get the effective group id, effective user id, real group id,
 a list of supplemental group ids associated with the current process."""

import os

print("gropup id: {}".format(os.getegid()))
print("effective user id: {}".format(os.getuid()))
print("real grouo id: {}".format(os.getgid()))
