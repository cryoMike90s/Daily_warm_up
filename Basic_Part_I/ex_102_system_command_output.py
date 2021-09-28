"""Write a Python program to get system command output."""

import subprocess

subprocess = subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
print(subprocess_return)