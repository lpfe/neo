#!/usr/bin/env python

def min(a, b) :
    if a < b :
        return a
    else :
        return b

a = int(input("Input first number : "))
b = int(input("Input second number : "))

print("{} vs {} : Min number = {}".format(a, b, min(a, b)))
