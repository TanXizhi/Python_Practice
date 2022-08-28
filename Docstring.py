#!/usr/bin/env python3
# doctring: a string at the beginning of a function and it is stored as part of the function

def square(x):
    'Calculate the square of the number x.'
    return x*x


print(square.__doc__)
