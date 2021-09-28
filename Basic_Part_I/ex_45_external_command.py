"""Write a python program to call an external command in Python."""

import subprocess



print(subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read())

return_code = subprocess.call("echo Hello World", shell=True)
print(return_code)

