#!/usr/bin/env python3
# Recursion: a function can call itself

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
