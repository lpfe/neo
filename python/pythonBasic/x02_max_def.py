#!/usr/bin/env python

import random

def findMax(data) :
    max = data[0]
    for i in range(1, len(data)) :
        if data[i] > max :
            max = data[i]
    return max

data = random.sample(range(1, 101), 10)

print(data)

print(f'Max is {findMax(data)}')

