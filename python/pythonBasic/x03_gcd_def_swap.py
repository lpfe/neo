#!/usr/bin/env python

def gcd(a, b):
    if a < b :
        a, b = b, a
    print(f'gcd({a}, {b})')
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

print(f'gcd({a}, {b}) = {gcd(a, b)}')