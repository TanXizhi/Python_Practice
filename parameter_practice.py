#!/usr/bin/env python3
# functions for supplying and receiving parameters

def story(**kwds):
    return 'Once upon a time, there was a '\
        '{job} called {name}.'.format_map(kwds)


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step >0'
    if stop is None:  # if the stop is not supplied
        start, stop = 0, start  # shuffle the parameters
    result = []
    i = start  # we start counting at the start index
    while i < stop:  # until the index reaches the stop index
        result.append(i)  # append the index to the result
        i += step  # increment the index with the step (>0)
    return result
