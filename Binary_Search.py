#!/usr/bin/env python3
# To find out whether a number is to be found in a (sorted) sequance and even to find out where it is

def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower+upper)//2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)
