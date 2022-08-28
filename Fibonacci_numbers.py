#!/usr/bin/env python3
# calculate Fibonacci numbers for a given number of range

def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

print('{}'.format(fibs(5)))
