#!/usr/bin/env python

def min(a, b) :
    return a if a < b else b

a = int(input("Input first number : "))
b = int(input("Input second number : "))

print("{} vs {} : Min number = {}".format(a, b, min(a, b)))
