#!/usr/bin/env python3
# To find the largest square below 100
# add an else clase to the loop---it is executed only if you didn't call break

from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it!")
