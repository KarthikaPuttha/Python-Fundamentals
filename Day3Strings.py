# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/167syL-uIsFgo24yO6wszTf23493Wwz6r

Strings
"""

name = 'karthika'

name2 = "karthika"

name3 = '''karthika'''

first_name = 'sai'

last_name = 'karthika'

full_name = 'sai puttha'

print(full_name)

print(full_name.title())

print(full_name.lower())

print(full_name.upper())

fullname = f"{first_name} {last_name}"
print(fullname)

print(f"keep up the good work, {first_name} {last_name}")

message = (f"keep up the good work, {first_name} {last_name}")
print(message.title())

"""Adding whitespaces to the string"""

print('fav food:coffeechickendosa')

print('fav food:\ncoffee\nchicken\ndosa')

"""\n it is called as new line delimiter """

print('fav food:\n\tcoffee\n\tchicken\n\tdosa')

"""\t it is called tab delimiter

Removing Whitespace from the string
"""

print('name')
print(' name')
print('name  ')

print('     name'.lstrip())

print('name     '.rstrip())