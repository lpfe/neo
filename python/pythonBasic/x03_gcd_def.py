#!/usr/bin/env python

def gcd(a, b):
    print(f'gcd({a}, {b}')
    while b != 0:
        r = a % b
        a = b
        b = r
    print(f'gcd({a}, {b}) = {a}')