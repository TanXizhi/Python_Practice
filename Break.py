#!/usr/bin/env python3
# To find the largest square below 100
# start at 100 and iterate downward to 0, when find the targeted square, there's
# no need to continue,so you simply break out of the loop.

from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
