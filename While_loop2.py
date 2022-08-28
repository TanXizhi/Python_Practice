#!/usr/bin/env python3
# use a while loop to ensure that the user enters a name

name = ' '
while not name or name.isspace():
    name = input('Enter your name: ')
print('Hello,{}!'.format(name))
