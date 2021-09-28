"""Write a Python program to access and print a URL's content to the console."""

import urllib.request


def my_url_content(path):
    return print((urllib.request.urlopen(path).read()))


path = 'https://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python'
my_url_content(path)